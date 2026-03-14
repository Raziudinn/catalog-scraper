import pandas as pd
import os
from scraper.crawler import CatalogCrawler
from scraper.parsers import parse_product_details
from scraper.utils import remove_duplicates

def main():
    crawler = CatalogCrawler()
    raw_data = []
    print("🚀 Starting Scraper...")

    # 1. Discover Categories
    categories = crawler.discover_categories()
    
    for cat in categories:
        print(f"📁 Processing Category: {cat['name']}")
        
        # 2. Discover Subcategories
        subcategories = crawler.discover_subcategories(cat['url'])
        
        for sub in subcategories:
            print(f"  ∟ 📂 Subcategory: {sub['name']}")
            
            # 3. Get Product Links (handles pagination automatically)
            product_links = crawler.get_product_links(sub['url'])
            
            for link in product_links:
                soup = crawler.get_soup(link)
                data = parse_product_details(soup, link, cat['name'], sub['name'])
                if data:
                    raw_data.append(data)

    # 4. Final Data Processing
    unique_data, dup_count = remove_duplicates(raw_data)
    
    # Ensure data directory exists
    os.makedirs("data", exist_ok=True)
    
    # 5. Export Products CSV
    df = pd.DataFrame(unique_data)
    df.to_csv("data/products.csv", index=False)
    
    # 6. Generate Summary CSV
    summary = df.groupby('subcategory').agg({
        'price': ['count', 'mean', 'min', 'max'],
        'description': lambda x: (x == "").sum()
    })
    summary.columns = ['total_products', 'avg_price', 'min_price', 'max_price', 'missing_descriptions']
    summary['duplicates_removed'] = dup_count
    summary.to_csv("data/category_summary.csv")

    print(f"\n✅ Success! Scraped {len(unique_data)} products.")
    print("Check the 'data' folder for your CSV files.")

if __name__ == "__main__":
    main()