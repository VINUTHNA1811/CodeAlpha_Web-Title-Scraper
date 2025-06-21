import requests
import re
import os
import logging
import sys

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_webpage(url):
    """Fetch webpage content"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        logging.info("Successfully fetched the webpage.")
        return response.text
    except requests.RequestException as e:
        logging.error(f"Error fetching the webpage: {e}")
        return None

def extract_title(html):
    """Extract the <title> tag using regex"""
    match = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE | re.DOTALL)
    if match:
        title = match.group(1).strip()
        logging.info(f"Title extracted: {title}")
        return title
    else:
        logging.warning("No <title> tag found in the HTML.")
        return "No Title Found"

def save_title(titles, output_file="titles.txt"):
    """Save the list of titles to a file"""
    try:
        with open(output_file, 'a', encoding='utf-8') as file:
            for title in titles:
                file.write(title + '\n')
        logging.info(f"Titles saved to {output_file}.")
    except Exception as e:
        logging.error(f"Error saving titles to file: {e}")

def is_valid_url(url):
    """Basic URL validation"""
    pattern = re.compile(
        r'^(?:http|https)://'  # http:// or https://
        r'(?:[\w\-]+\.)+[a-z]{2,6}'  # domain
        r'(?:/[\w\-.~:/?#\[\]@!$&\'()*+,;=%]*)?$', re.IGNORECASE)
    return re.match(pattern, url) is not None

def main():
    logging.info("Web Title Scraper Started.")

    titles = []

    while True:
        url = input("Enter website URL (or type 'done' to finish): ").strip()

        if url.lower() == 'done':
            break

        if not is_valid_url(url):
            logging.error("Invalid URL format. Please enter a valid URL starting with http:// or https://")
            continue

        html = fetch_webpage(url)
        if html:
            title = extract_title(html)
            print(f"Website Title: {title}")
            titles.append(f"{url} - {title}")
        else:
            logging.error("Failed to fetch webpage.")

    if titles:
        save_permission = input("Do you want to save all extracted titles to file? (yes/no): ").strip().lower()
        if save_permission == 'yes':
            save_title(titles)
            print("Titles saved successfully!")
        else:
            print("Titles not saved.")
    else:
        print("No titles extracted.")

if __name__ == "__main__":
    main()
