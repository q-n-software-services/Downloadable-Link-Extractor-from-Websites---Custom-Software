import requests
from bs4 import BeautifulSoup
import re
import time
import os

# Function to extract downloadable links from a webpage
def extract_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    for link in soup.find_all('a', href=True):
        if re.search(r'\.(pdf|jpg|png|mp3|mp4)$', link['href']):
            links.append(link['href'])
    return links

# Function to crawl through the website and extract links
def crawl_website(url):
    visited_urls = set()
    links_to_visit = [url]
    while links_to_visit:
        current_url = links_to_visit.pop(0)
        if current_url in visited_urls:
            continue
        visited_urls.add(current_url)
        try:
            links = extract_links(current_url)
            with open('extracted_links.txt', 'a') as f:
                for link in links:
                    f.write(link + '\n')
            response = requests.get(current_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            for link in soup.find_all('a', href=True):
                if link['href'].startswith('/'):
                    link = url + link['href']
                if link['href'].startswith(url):
                    links_to_visit.append(link['href'])
        except:
            pass

# Get website URL from user input
url = input('Enter website URL: ')

# Create file to store extracted links
filename = 'extracted_links_{}.txt'.format(str(time.time()).split('.')[0])
with open(filename, 'w'):
    pass

# Crawl website and extract links
crawl_website(url)

print('Links extracted and saved in file: {}'.format(filename))
