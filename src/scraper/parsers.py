from .utils import normalize_price, clean_text
from urllib.parse import urljoin

def parse_product_details(soup, url, category, subcategory):
    if not soup: return None
    title = soup.select_one(".caption h4:nth-child(2)")
    price = soup.select_one(".caption h4.pull-right")
    desc = soup.select_one(".caption p.description")
    reviews = soup.select_one(".ratings p.pull-right")
    img = soup.select_one(".thumbnail img")

    return {
        "category": category,
        "subcategory": subcategory,
        "product_title": clean_text(title.text) if title else "N/A",
        "price": normalize_price(price.text) if price else 0.0,
        "product_url": url,
        "image_url": urljoin(url, img['src']) if img else "N/A",
        "description": clean_text(desc.text) if desc else "",
        "review_count": clean_text(reviews.text) if reviews else "0 reviews",
        "source_page": url
    }