# Manga-Scraper

Manga-Scraper is a webscraping tool for downloading manga panels. Its main goal is to be as general as possible so that scraping different mangas becomes easier.

Note: This tool only works iff the following rules are true:

1. The chapter URLs have the form: string {chapter name} string
2. All Manga panels have to be shown on the site.
3. All panels have to share the same html class name (which is almost always the case)


## How it works

![image](https://user-images.githubusercontent.com/46029684/204039536-4b248310-1897-4370-9973-344c779920fe.png)

## Example

```python
url_format = "https://ww4.readdrstone.com/chapter/dr-stone-chapter-{}/"
chapter_names = [str(i) for i in list(range(1, 10))]

scraper = Scraper(url_format, chapter_names)
chapters = scraper.scrape()

downloader = Downloader("Dr Stone", info=True)
downloader.download(chapters, make_zip=True)
```


# Classes

## Scraper
```java
String chapter_url_format;
String[] chapters_spelling;
Chapter[] chapters;
PanelFinder panel_finder;

public Chapter[] scrape;
```

## PanelFinder
```java
public String[] findPanels //(returns URLs of manga panels, mostly jpegs)
```

## Chapter
```java
String spelling; //name of chapter
String URL;
Panel[] panels;
```

## Panel
```java
int ID; //indicates the order of panels in a chapter
String url; //image url
Chapter parent_chapter;
```

## Downloader
```java
public void download //Creates directory and downloads images
public void zip //Creates zip archive
```
