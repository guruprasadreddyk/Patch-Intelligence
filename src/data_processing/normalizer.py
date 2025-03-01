# src/data_processing/normalizer.py
import pandas as pd

def normalize_patch_data(patch_df: pd.DataFrame) -> pd.DataFrame:
    # Standardize vendor and product names (example: convert to lowercase and trim)
    if 'vendor' in patch_df.columns:
        patch_df['vendor'] = patch_df['vendor'].str.lower().str.strip()
    if 'product' in patch_df.columns:
        patch_df['product'] = patch_df['product'].str.lower().str.strip()
    # Additional normalization can be added here (e.g., version formatting)
    return patch_df

if __name__ == "__main__":
    import pandas as pd
    sample_data = {'vendor': ['VendorX ', ' VendorY'], 'product': ['ProductA', 'ProductB']}
    df = pd.DataFrame(sample_data)
    print(normalize_patch_data(df))
