# tests/test_vendor_scraper.py
import pytest
import pandas as pd
from src.data_collection.vendor_scraper import fetch_vendor_patch_info

def test_fetch_vendor_patch_info(monkeypatch):
    # Create a fake HTML response
    fake_html = """
    <html>
      <body>
        <div class="patch-entry">
          <span class="vendor">VendorX</span>
          <span class="product">ProductA</span>
          <span class="version">1.2.3</span>
          <a class="details" href="https://example.com/patches/1">Details</a>
        </div>
      </body>
    </html>
    """
    class FakeResponse:
        def __init__(self, text):
            self.text = text
        def raise_for_status(self):
            pass
    monkeypatch.setattr("src.data_collection.vendor_scraper.requests.get", lambda url, timeout: FakeResponse(fake_html))
    
    df = fetch_vendor_patch_info("https://fakeurl.com")
    assert not df.empty
    assert "vendor" in df.columns
    assert df.iloc[0]["vendor"] == "VendorX"
