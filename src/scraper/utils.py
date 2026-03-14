import re

def clean_text(text):
    if not text: return ""
    return " ".join(text.split())

def normalize_price(price_string):
    if not price_string: return 0.0
    try:
        numeric_part = re.sub(r'[^\d.]', '', price_string)
        return float(numeric_part)
    except ValueError:
        return 0.0

def remove_duplicates(data_list):
    seen = set()
    unique_data = []
    duplicates_count = 0
    for item in data_list:
        if item['product_url'] not in seen:
            unique_data.append(item)
            seen.add(item['product_url'])
        else:
            duplicates_count += 1
    return unique_data, duplicates_count