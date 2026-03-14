Project Report: E-Commerce Catalog Scraper

1. Documentation of Branching Workflow

To fulfill the requirement for a clean and traceable development history, I followed a professional branching model:

main: The stable production branch containing the final, documented code.

dev: The integration branch where features and fixes were merged.

feature/catalog-navigation: Developed the core traversal logic for categories, subcategories, and pagination.

fix/url-resolution: Verified absolute URL generation for images and product links.

fix/deduplication: Implemented and tested logic to prevent redundant data entries.

2. Technical Implementation

Reproducibility: Managed with uv to ensure consistent environments.

Scraping: Utilized BeautifulSoup4 for hierarchical navigation and detail-page extraction.

Data Quality:

Prices normalized from strings to floats for statistical summaries.

White-space cleaning for professional CSV output.

Deduplication based on unique product URLs.

3. Generated Deliverables

data/products.csv: Comprehensive product list with deep-scraped descriptions.

data/category_summary.csv: Aggregated report with counts and price statistics.