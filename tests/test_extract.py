from pathlib import Path

from pipeline.extract import extract_customers


def test_extract_customers():
    file_path = Path("data/customers.csv")

    df = extract_customers(file_path)

    assert not df.empty
    assert len(df) == 5
    assert "customer_id" in df.columns
    assert "name" in df.columns
    assert "email" in df.columns
    assert "age" in df.columns