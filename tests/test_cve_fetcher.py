# tests/test_cve_fetcher.py
import pytest
import pandas as pd
from src.data_collection.cve_fetcher import fetch_cve_data

def test_fetch_cve_data(monkeypatch):
    fake_json = {
        "result": {
            "CVE_Items": [
                {
                    "cve": {
                        "CVE_data_meta": {"ID": "CVE-2023-XXXX"},
                        "description": {"description_data": [{"value": "Sample vulnerability description"}]}
                    }
                }
            ]
        }
    }
    class FakeResponse:
        def __init__(self, json_data):
            self._json = json_data
        def raise_for_status(self):
            pass
        def json(self):
            return self._json
    monkeypatch.setattr("src.data_collection.cve_fetcher.requests.get", lambda url, params, timeout: FakeResponse(fake_json))
    
    df = fetch_cve_data("https://fakeapi.com")
    assert not df.empty
    assert "cve_id" in df.columns
    assert df.iloc[0]["cve_id"] == "CVE-2023-XXXX"
