from urllib.parse import urlparse
import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import requests
import urllib.request
import urllib.error
import urllib.parse


class FeatureExtractor:
    def __init__(self, url):
        self.url = url
    
    def google_index(url):
        try:
            query = {'q': 'info:' + url}
            google = "https://www.google.com/search?" + urllib.parse.urlencode(query)
            hdr = {'User-Agent': 'Mozilla/5.0'}
            req = urllib.request.Request(google, headers=hdr)
            page = urllib.request.urlopen(req)
            soup = BeautifulSoup(page, "html.parser")
            return int(soup.find('div', {'id': 'resultStats'}).text.replace(',', '').split()[1])
        except:
            return -1

    def ratio_intHyperlinks(url):
        try:
            html_content = requests.get(url).text
            soup = BeautifulSoup(html_content, "html.parser")
            urls = []
            for tag in soup.findAll('a', href=True):
                urls.append(tag['href'])
            count = 0
            for url in urls:
                if url.startswith("https://") or url.startswith("http://"):
                    count = count + 1
            return count/len(urls)
        except:
            return -1

    def nb_hyperlinks(url):
        try:
            html_content = requests.get(url).text
            soup = BeautifulSoup(html_content, "html.parser")
            urls = []
            for tag in soup.findAll('a', href=True):
                urls.append(tag['href'])
            count = 0
            for url in urls:
                if url.startswith("https://") or url.startswith("http://"):
                    count = count + 1
            return count
        except:
            return -1

    def ratio_digits_url(url):
        try:
            digits = 0
            for i in url:
                if i.isnumeric():
                    digits = digits + 1
            return digits/len(url)
        except:
            return -1

    def nb_www(url):
        try:
            return url.count('www')
        except:
            return -1

    def nb_slash(url):
        try:
            return url.count('/')
        except:
            return -1

    def length_hostname(url):
        try:
            return len(urlparse(url).netloc)
        except:
            return -1

    def length_url(url):
        try:
            return len(url)
        except:
            return -1


    def extract_features(self):
        features = []
        features.append(self.google_index())
        features.append(self.ratio_intHyperlinks())
        features.append(self.nb_hyperlinks())
        features.append(self.ratio_digits_url())
        features.append(self.nb_www())
        features.append(self.nb_slash())
        features.append(self.length_hostname())
        features.append(self.length_url())
        return features