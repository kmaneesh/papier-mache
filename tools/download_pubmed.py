"""
download_pubmed.py

Searches and downloads references from PubMed.

Usage:
    python download_pubmed.py --query "search term" --max_results 10 --output_dir "data/download"

Parameters:
    --query: Search term for PubMed
    --max_results: Maximum number of results to download (default: 10)
    --output_dir: Directory to store downloaded papers (default: data/download)
"""
import requests
import os
import argparse

def search_pubmed(query, max_results=10):
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={query}&retmax={max_results}&retmode=json"
    response = requests.get(url)
    response.raise_for_status()
    ids = response.json()['esearchresult']['idlist']
    return ids

def download_papers(ids, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for pmid in ids:
        # PubMed does not provide direct PDF links, so we download metadata
        file_path = os.path.join(output_dir, f"pubmed_{pmid}.txt")
        url = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
        try:
            r = requests.get(url)
            r.raise_for_status()
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(r.text)
            print(f"Downloaded metadata: {file_path}")
        except Exception as e:
            print(f"Failed to download {url}: {e}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--query', required=True)
    parser.add_argument('--max_results', type=int, default=10)
    parser.add_argument('--output_dir', default='data/download')
    args = parser.parse_args()
    ids = search_pubmed(args.query, args.max_results)
    download_papers(ids, args.output_dir)

if __name__ == '__main__':
    main()
