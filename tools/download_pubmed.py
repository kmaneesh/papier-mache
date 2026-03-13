"""
download_pubmed.py

Searches and downloads references from PubMed as Markdown including abstracts.

Usage:
    python download_pubmed.py --query "search term" --max_results 10 --output_dir "data/download"
"""
import requests
import os
import argparse
import urllib.parse
import json
import time

def search_pubmed(query, max_results=10):
    query_encoded = urllib.parse.quote(query)
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={query_encoded}&retmax={max_results}&retmode=json"
    response = requests.get(url)
    response.raise_for_status()
    ids = response.json()['esearchresult']['idlist']
    return ids

def fetch_abstract(pmid):
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={pmid}&retmode=text&rettype=abstract"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text.strip()
    except Exception as e:
        print(f"Failed to fetch abstract for {pmid}: {e}")
        return ""

def fetch_details(ids):
    if not ids:
        return []
    id_list = ",".join(ids)
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id={id_list}&retmode=json"
    response = requests.get(url)
    response.raise_for_status()
    result = response.json().get('result', {})
    uids = result.get('uids', [])
    papers = []
    for uid in uids:
        if uid in result:
            paper = result[uid]
            # Fetch abstract separately
            paper['abstract'] = fetch_abstract(uid)
            papers.append(paper)
            time.sleep(0.3) # Rate limiting
    return papers

def save_as_md(papers, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for paper in papers:
        pmid = paper.get('uid')
        title = paper.get('title', 'No Title').strip('.')
        authors = ", ".join([a.get('name') for a in paper.get('authors', [])])
        source = paper.get('source', '')
        pubdate = paper.get('pubdate', '')
        doi = ""
        for articleid in paper.get('articleids', []):
            if articleid.get('idtype') == 'doi':
                doi = articleid.get('id')
        
        abstract = paper.get('abstract', '')
        
        md_content = f"# {title}\n\n"
        md_content += f"**PMID**: {pmid}\n"
        if doi:
            md_content += f"**DOI**: [{doi}](https://doi.org/{doi})\n"
        md_content += f"**Link**: [PubMed](https://pubmed.ncbi.nlm.nih.gov/{pmid}/)\n"
        md_content += f"**Authors**: {authors}\n"
        md_content += f"**Source**: {source} ({pubdate})\n\n"
        
        if abstract:
            md_content += "## Abstract\n"
            md_content += f"{abstract}\n"
        else:
            md_content += "## Summary\n"
            md_content += f"Abstract not available for PMID {pmid}.\n"
        
        file_path = os.path.join(output_dir, f"pubmed_{pmid}.md")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print(f"Saved: {file_path}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--query', required=True)
    parser.add_argument('--max_results', type=int, default=10)
    parser.add_argument('--output_dir', default='data/download')
    args = parser.parse_args()
    
    ids = search_pubmed(args.query, args.max_results)
    if ids:
        papers = fetch_details(ids)
        save_as_md(papers, args.output_dir)
    else:
        print("No results found.")

if __name__ == '__main__':
    main()
