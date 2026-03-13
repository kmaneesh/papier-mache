"""
download_arxiv.py

Searches and downloads references from arXiv.

Usage:
    python download_arxiv.py --query "search term" --max_results 10 --output_dir "data/download"

Parameters:
    --query: Search term for arXiv
    --max_results: Maximum number of results to download (default: 10)
    --output_dir: Directory to store downloaded papers (default: data/download)
"""
import os
import argparse
import requests
import feedparser

def search_arxiv(query, max_results=10):
    url = f"http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results={max_results}"
    feed = feedparser.parse(url)
    return feed.entries

def download_papers(entries, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for entry in entries:
        pdf_url = entry.get('links', [{}])[-1].get('href', '')
        arxiv_id = entry.get('id', '').split('/')[-1]
        file_path = os.path.join(output_dir, f"arxiv_{arxiv_id}.pdf")
        if pdf_url.endswith('.pdf'):
            try:
                r = requests.get(pdf_url)
                r.raise_for_status()
                with open(file_path, 'wb') as f:
                    f.write(r.content)
                print(f"Downloaded: {file_path}")
            except Exception as e:
                print(f"Failed to download {pdf_url}: {e}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--query', required=True)
    parser.add_argument('--max_results', type=int, default=10)
    parser.add_argument('--output_dir', default='data/download')
    args = parser.parse_args()
    entries = search_arxiv(args.query, args.max_results)
    download_papers(entries, args.output_dir)

if __name__ == '__main__':
    main()
