# core/website.py
import requests
from bs4 import BeautifulSoup

class Website:
    def __init__(self, url):
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        self.title = soup.title.string if soup.title else 'No title found'
        
        for tag in soup(['script', 'style', 'img', 'input']):
            tag.decompose()
        
        self.text = ' '.join(soup.body.stripped_strings) if soup.body else ''