import requests
from bs4 import BeautifulSoup
import os
import urllib.request
import shutil




class Scraper:
    def __init__(self, chapter_url_format:str, chapters_spelling:str, panel_finder=None):
        self.chapter_url_format = chapter_url_format
        self.chapters_spelling = chapters_spelling
        self.chapters = []
        self.panel_finder = PanelFinder() if panel_finder is None else panel_finder

    def scrape(self):
        for chapter_spelling in self.chapters_spelling:
            chapter_url = self.chapter_url_format.format(chapter_spelling)
            chapter = Chapter(chapter_spelling, chapter_url, [])

            r = requests.get(chapter_url)
            chapter.panels = self.panel_finder.findPanels(r, chapter)

            if len(chapter.panels) == 0:
                continue

            self.chapters.append(chapter)

        return self.chapters


class PanelFinder:
    def __init__(self, class_selector="mb-3 mx-auto js-page"):
        self.class_selector = class_selector

    def findPanels(self, request, parent_chapter):
        soup = BeautifulSoup(request.content, 'html.parser')
        images = soup.findAll('img', {'class': self.class_selector})
        images = [Panel(i+1, img['src'], parent_chapter) for i, img in enumerate(images)]
        return images


class Chapter:
    def __init__(self, spelling:str, url:str, panels):
        self.spelling = spelling
        self.url = url
        self.panels = panels


class Panel:
    def __init__(self, ID:int, url:str, parent_chapter:Chapter):
        self.ID = ID
        self.url = url
        self.parent_chapter = parent_chapter


class Downloader:
    def __init__(self, dir_name, path=None, info=False):
        self.dir_name = dir_name #name of the manga to download
        self.path = os.path.join(os.path.dirname(__file__), self.dir_name) if path is None else path
        self.info = info
        self.finished = False
        self.suffix = "jpeg"

    def download(self, chapters, make_zip=False):
        if not os.path.exists(self.path):
            os.mkdir(self.path)

        for ch in chapters:
            chapter_path = os.path.join(self.path, "CH_" + str(ch.spelling))

            if not os.path.exists(chapter_path):
                os.mkdir(chapter_path)
            elif len(os.listdir(chapter_path)) == len(ch.panels):
                if self.info:
                    print(f"Chapter {ch.spelling} already done!")
                continue

            if self.info:
                print(f"Downloading chapter {ch.spelling}...")
            for p in ch.panels:
                img_file_name = f'{p.ID:04}.{self.suffix}'
                img_save_path = os.path.join(chapter_path, img_file_name)

                try:
                    #urllib.request.urlretrieve(img_url, img_save_6path)
                    r = requests.get(p.url)
                    with open(img_save_path, 'wb') as outfile:
                        outfile.write(r.content)

                        if self.info:
                            print(f"Download Successfull {p.ID} {p.url}")

                except urllib.error.HTTPError as exception:
                    continue

        self.finished = True

        if make_zip:
            self.zip()

    def zip(self):
        if not self.finished:
            return

        if self.info:
            print("Creating zip file...")

        shutil.make_archive(self.dir_name, 'zip', os.path.dirname(__file__), self.dir_name)

        if self.info:
            print("zip file ready!")
