"""
download_openalex.py

Searches and downloads references from OpenAlex.

Usage:
    python download_openalex.py --query "search term" --max_results 10 --output_dir "data/download"

Parameters:
    --query: Search term for OpenAlex
    --max_results: Maximum number of results to download (default: 10)
    --output_dir: Directory to store downloaded papers (default: data/download)
"""
import requests
import os
import argparse

def search_openalex(query, max_results=10):
    url = f"https://api.openalex.org/works?search={query}&per_page={max_results}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json().get('results', [])

def download_papers(results, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for item in results:
        pdf_url = item.get('pdf_url')
        if pdf_url:
            paper_id = item.get('id', 'unknown').split('/')[-1]
            file_path = os.path.join(output_dir, f"openalex_{paper_id}.pdf")
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
    results = search_openalex(args.query, args.max_results)
    download_papers(results, args.output_dir)

if __name__ == '__main__':
    main()
