"""
download_arxiv.py

Searches and downloads references from arXiv as Markdown.

Usage:
    python download_arxiv.py --query "search term" --max_results 10 --output_dir "data/download"
"""
import os
import argparse
import requests
import feedparser
import urllib.parse

def search_arxiv(query, max_results=10):
    query_encoded = urllib.parse.quote(query)
    url = f"http://export.arxiv.org/api/query?search_query=all:{query_encoded}&start=0&max_results={max_results}"
    feed = feedparser.parse(url)
    return feed.entries

def save_as_md(entries, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for entry in entries:
        arxiv_id = entry.get('id', '').split('/')[-1]
        title = entry.get('title', 'No Title').replace('\n', ' ').strip()
        authors = ", ".join([a.get('name', '') for a in entry.get('authors', [])])
        summary = entry.get('summary', '').replace('\n', ' ').strip()
        published = entry.get('published', '')
        doi = entry.get('arxiv_doi', '')
        links = entry.get('links', [])
        pdf_url = ""
        for link in links:
            if link.get('title') == 'pdf' or link.get('type') == 'application/pdf':
                pdf_url = link.get('href', '')

        md_content = f"# {title}\n\n"
        md_content += f"**arXiv ID**: [{arxiv_id}]({entry.get('id')})\n"
        if doi:
            md_content += f"**DOI**: [{doi}](https://doi.org/{doi})\n"
        md_content += f"**Authors**: {authors}\n"
        md_content += f"**Published**: {published}\n"
        if pdf_url:
            md_content += f"**PDF Link**: [{pdf_url}]({pdf_url})\n"
        md_content += "\n"
        
        md_content += "## Abstract\n"
        md_content += f"{summary}\n"
        
        file_path = os.path.join(output_dir, f"arxiv_{arxiv_id}.md")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print(f"Saved: {file_path}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--query', required=True)
    parser.add_argument('--max_results', type=int, default=10)
    parser.add_argument('--output_dir', default='data/download')
    args = parser.parse_args()
    
    entries = search_arxiv(args.query, args.max_results)
    if entries:
        save_as_md(entries, args.output_dir)
    else:
        print("No results found.")

if __name__ == '__main__':
    main()
