import sys
from pathlib import Path

import requests
from bs4 import BeautifulSoup


def fetch_html(url: str, timeout_seconds: int = 15) -> str:
	"""Fetch raw HTML from the given URL and return text. Raises on HTTP errors."""
	response = requests.get(url, timeout=timeout_seconds, headers={
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
	})
	response.raise_for_status()
	return response.text


def parse_headlines(html: str) -> list[str]:
	"""Parse likely headline texts from HTML using common tags/classes."""
	soup = BeautifulSoup(html, "html.parser")
	headlines: list[str] = []

	# Common headline tags in many news sites
	for tag_name in ["h1", "h2", "h3"]:
		for tag in soup.find_all(tag_name):
			text = tag.get_text(strip=True)
			if not text:
				continue
			# filter out boilerplate
			if len(text) < 5:
				continue
			headlines.append(text)

	# De-duplicate while preserving order
	seen = set()
	unique_headlines: list[str] = []
	for h in headlines:
		if h in seen:
			continue
		seen.add(h)
		unique_headlines.append(h)

	return unique_headlines


def save_headlines(headlines: list[str], output_path: Path) -> None:
	output_path.write_text("\n".join(headlines), encoding="utf-8")


def main() -> int:
	# Default to a public, widely accessible news homepage
	default_url = "https://www.bbc.com/news"
	url = sys.argv[1] if len(sys.argv) > 1 else default_url

	try:
		html = fetch_html(url)
	except Exception as exc:
		print(f"Error fetching {url}: {exc}")
		return 1

	headlines = parse_headlines(html)
	if not headlines:
		print("No headlines found. Try another URL or adjust parsing.")
		return 2

	output_path = Path("headlines.txt")
	save_headlines(headlines, output_path)
	print(f"Saved {len(headlines)} headlines to {output_path.resolve()}")
	return 0


if __name__ == "__main__":
	sys.exit(main())


