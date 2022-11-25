# Manga-Scraper

Manga-Scraper is a webscraping tool for downloading manga panels. Its main goal is to be as general as possible so that scraping different mangas becomes easier.


## How it works

picture

## Example

```python
chapter_names = [str(i) for i in list(range(1, 10))]
scraper = Scraper("https://ww4.readdrstone.com/chapter/dr-stone-chapter-{}/", chapter_names, panel_finder=PanelFinder2())
chapters = scraper.scrape()

downloader = Downloader("dr stone", info=True)
downloader.download(chapters, make_zip=True)
```
