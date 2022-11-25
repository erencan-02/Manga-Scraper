# Manga-Scraper

Manga-Scraper is a webscraping tool for downloading manga panels. Its main goal is to be as general as possible so that scraping different mangas becomes easier.


## How it works

![image](https://user-images.githubusercontent.com/46029684/204039536-4b248310-1897-4370-9973-344c779920fe.png)

## Example

```python
url_format = "https://ww4.readdrstone.com/chapter/dr-stone-chapter-{}/"
chapter_names = [str(i) for i in list(range(1, 10))]

scraper = Scraper(url_format, chapter_names, panel_finder=PanelFinder2())
chapters = scraper.scrape()

downloader = Downloader("dr stone", info=True)
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
public String[] findPanels //(returns URLs of manga panels)
```

## Chapter
```java
String spelling;
String URL;
Panel[] panels;
```

## Panel
```java
int ID;
String url;
Chapter parent_chapter;
```

## Downloader
```java
public void download
public void zip
```
