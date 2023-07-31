import httplib2
import os
import re
import threading
import urllib
import urllib.request
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup


class CrawlerSingleton:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(CrawlerSingleton, cls).__new__(cls)
        return cls.instance
    


def navigate_site(max_links =5):
    parser_crawl = CrawlerSingleton()
    
    while parser_crawl.url_queue:
        if len(parser_crawl.visited_url) == max_links:
            return
        url = parser_crawl.url_queue.pop()
        http = httplib2.Http()
        try:
            status, response = http.request(url)
        except Exception:
            continue

        parser_crawl.visited_url.add(url)
        print(url)

        bs = BeautifulSoup(response, "html.parser")
        for link in BeautifulSoup.findAll(bs, 'a'):
            link_url = link.get('href')
            if not link_url:
                continue
            parsed = urlparse(link_url)
            if parsed.netloc and parsed.netloc != parsed_url.netloc:
                continue
            schema = parsed_url.scheme
            netloc = parsed.netloc or parsed_url.netloc
            path = parsed.path
            link_url = schema + '://' + netloc +path

            if link_url in parser_crawl.visited_url:
                continue

            parser_crawl.url_queue = [link_url] + parser_crawl.url_queue


class ParallelDownloader(threading.Thread):
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.name =name
    
    def run(self):
        print("starting thread ", self.name)
        download_images(self.name)
        print("finished downloading ", self.name)
    

def download_images(thread_name):
    singleton = CrawlerSingleton()
    while singleton.visited_url:
        url = singleton.visited_url.pop()
        http = httplib2.Http()
        
        try:
            statuts, response = http.request(url)
        except Exception:
            continue

        bs = BeautifulSoup(response, "html.parser")
        images = BeautifulSoup.findAll(bs, 'img')

        for image in images:
            src = image.get('src')
            src = urljoin(url, src)

            basename = os.path.basename(src)
            print("basename ", basename)
            if basename != "":
                if src not in singleton.image_downloaded:
                    singleton.image_downloaded.add(src)
                    print('Downloading', src)
                    urllib.request.urlretrieve(src, os.path.join('images', basename))
                    
def main():
    crawl = CrawlerSingleton()
    crawl.url_queue = [main_url]
    crawl.visited_url = set()
    crawl.image_downloaded = set()
    navigate_site()
    if not os.path.exists('images'):
        os.makedirs('images')
    therad1 = ParallelDownloader(1, "Thread1",1)
    therad2 = ParallelDownloader(2, "Thread2",2)
    therad1.start()

    therad2.start()

main_url = ("https://www.geeksforgeeks.org/")
parsed_url = urlparse(main_url)
main()