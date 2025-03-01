# src/data_collection/vendor_scraper.py
import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging
from src.config import VENDOR_PATCH_URL

logger = logging.getLogger(__name__)

def fetch_vendor_patch_info(url=VENDOR_PATCH_URL) -> pd.DataFrame:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        logger.error(f"Request failed: {e}")
        return pd.DataFrame()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    patch_data = []
    
    # Customize the selectors based on the vendor's HTML structure
    for entry in soup.find_all('div', class_='patch-entry'):
        try:
            vendor = entry.find('span', class_='vendor').get_text(strip=True)
            product = entry.find('span', class_='product').get_text(strip=True)
            fixed_version = entry.find('span', class_='version').get_text(strip=True)
            patch_url = entry.find('a', class_='details')['href']
            patch_data.append({
                'vendor': vendor,
                'product': product,
                'fixed_version': fixed_version,
                'patch_url': patch_url
            })
        except AttributeError as e:
            logger.warning(f"Missing data in entry: {e}")
    
    return pd.DataFrame(patch_data)

if __name__ == "__main__":
    df = fetch_vendor_patch_info()
    print(df.head())
