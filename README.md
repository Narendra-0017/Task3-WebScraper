# Task 3: Web Scraper for News Headlines

A simple Python script that fetches a news homepage, parses common headline tags, and saves them to `headlines.txt`.

## Requirements
- Python 3.8+ (tested on Python 3.13)

## Install Dependencies (PowerShell)
```powershell
cd C:\Users\naren\Downloads\Task3
python -m pip install --upgrade pip
python -m pip install requests beautifulsoup4
```

## Run
- Default (BBC News):
```powershell
cd C:\Users\naren\Downloads\Task3
python scrape_headlines.py
```
- Custom site (example: Reuters):
```powershell
python scrape_headlines.py https://www.reuters.com
```

This will create/update `headlines.txt` in the same directory.

## How it works
- Uses `requests` to fetch HTML
- Uses `BeautifulSoup` to parse `<h1>`, `<h2>`, `<h3>` tags
- De-duplicates headlines and writes them to `headlines.txt`

## Notes
- Sites differ in structure; if a site uses custom classes or non-standard tags, parsing may need minor adjustments in `scrape_headlines.py`.
- Respect the website's terms of service and `robots.txt`.
- Network restrictions or captive portals can cause fetch errors.

## File overview
- `scrape_headlines.py` — main script
- `headlines.txt` — output file with one headline per line
