"""
download_openalex.py

Searches and downloads references from OpenAlex as Markdown.

Usage:
    python download_openalex.py --query "search term" --max_results 10 --output_dir "data/download"
"""
import requests
import os
import argparse
import urllib.parse

def search_openalex(query, max_results=10):
    query_encoded = urllib.parse.quote(query)
    url = f"https://api.openalex.org/works?search={query_encoded}&per_page={max_results}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json().get('results', [])

def save_as_md(results, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for item in results:
        paper_id = item.get('id', 'unknown').split('/')[-1]
        title = item.get('display_name', 'No Title')
        doi = item.get('doi', '')
        pub_year = item.get('publication_year', '')
        authors = ", ".join([a.get('author', {}).get('display_name', '') for a in item.get('authorships', [])])
        concepts = ", ".join([c.get('display_name', '') for c in item.get('concepts', [])[:5]])
        abstract_inverted_index = item.get('abstract_inverted_index')
        
        abstract = ""
        if abstract_inverted_index:
            # Reconstruct abstract from inverted index
            word_list = []
            for word, positions in abstract_inverted_index.items():
                for pos in positions:
                    word_list.append((pos, word))
            word_list.sort()
            abstract = " ".join([w[1] for w in word_list])

        md_content = f"# {title}\n\n"
        md_content += f"**OpenAlex ID**: [{paper_id}]({item.get('id')})\n"
        if doi:
            md_content += f"**DOI**: [{doi}]({doi})\n"
        md_content += f"**Authors**: {authors}\n"
        md_content += f"**Publication Year**: {pub_year}\n"
        md_content += f"**Key Concepts**: {concepts}\n\n"
        
        if abstract:
            md_content += "## Abstract\n"
            md_content += f"{abstract}\n"
        else:
            md_content += "## Summary\n"
            md_content += "This is a structured metadata record for an OpenAlex work.\n"
        
        file_path = os.path.join(output_dir, f"openalex_{paper_id}.md")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print(f"Saved: {file_path}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--query', required=True)
    parser.add_argument('--max_results', type=int, default=10)
    parser.add_argument('--output_dir', default='data/download')
    args = parser.parse_args()
    
    results = search_openalex(args.query, args.max_results)
    if results:
        save_as_md(results, args.output_dir)
    else:
        print("No results found.")

if __name__ == '__main__':
    main()
