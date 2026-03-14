import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class CatalogCrawler:
    BASE_URL = "https://webscraper.io/test-sites/e-commerce/static"

    def __init__(self):
        self.session = requests.Session()

    def get_soup(self, url):
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            return BeautifulSoup(response.text, 'html.parser')
        except:
            return None

    def discover_categories(self):
        soup = self.get_soup(self.BASE_URL)
        if not soup: return []
        links = soup.select("#side-menu > li > a.category-link")
        return [{"name": a.text.strip(), "url": urljoin(self.BASE_URL, a['href'])} for a in links]

    def discover_subcategories(self, category_url):
        soup = self.get_soup(category_url)
        if not soup: return []
        links = soup.select("#side-menu > li.active > ul > li > a")
        return [{"name": a.text.strip(), "url": urljoin(self.BASE_URL, a['href'])} for a in links]

    def get_product_links(self, sub_url):
        links, curr = [], sub_url
        while curr:
            soup = self.get_soup(curr)
            if not soup: break
            links.extend([urljoin(self.BASE_URL, a['href']) for a in soup.select(".caption h4 > a")])
            next_btn = soup.select_one("ul.pagination li:last-child a")
            curr = urljoin(self.BASE_URL, next_btn['href']) if next_btn and "»" in next_btn.text else None
        return links