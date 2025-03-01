# src/data_collection/cve_fetcher.py
import requests
import pandas as pd
import logging
from src.config import CVE_API_URL

logger = logging.getLogger(__name__)

def fetch_cve_data(api_url=CVE_API_URL) -> pd.DataFrame:
    params = {'resultsPerPage': 100}
    try:
        response = requests.get(api_url, params=params, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        logger.error(f"Error fetching CVE data: {e}")
        return pd.DataFrame()
    
    cve_json = response.json()
    cve_data = []
    
    for item in cve_json.get('result', {}).get('CVE_Items', []):
        cve_id = item.get('cve', {}).get('CVE_data_meta', {}).get('ID')
        description = item.get('cve', {}).get('description', {}).get('description_data', [{}])[0].get('value')
        cve_data.append({'cve_id': cve_id, 'description': description})
    
    return pd.DataFrame(cve_data)

if __name__ == "__main__":
    df = fetch_cve_data()
    print(df.head())
