# src/data_processing/correlator.py
import pandas as pd

def correlate_patch_cve(patch_df: pd.DataFrame, cve_df: pd.DataFrame) -> pd.DataFrame:
    # Merge on vendor and product columns
    correlated_df = pd.merge(patch_df, cve_df, how='left', left_on=['vendor', 'product'], right_on=['vendor', 'product'])
    return correlated_df

if __name__ == "__main__":
    # Dummy data for testing the correlation
    patch_df = pd.DataFrame({
        'vendor': ['vendorx', 'vendory'],
        'product': ['producta', 'productb'],
        'fixed_version': ['1.2.3', '2.3.4']
    })
    cve_df = pd.DataFrame({
        'vendor': ['vendorx', 'vendory'],
        'product': ['producta', 'productb'],
        'cve_id': ['CVE-2023-XXXX', 'CVE-2023-YYYY']
    })
    print(correlate_patch_cve(patch_df, cve_df))
