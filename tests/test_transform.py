import pandas as pd

from pipeline.transform import transform_customers


def test_transform_customers():
    df = pd.DataFrame(
        {
            "customer_id": [1],
            "name": ["  john doe  "],
            "email": [" JOHN@EXAMPLE.COM "],
            "age": [28],
        }
    )

    result = transform_customers(df)

    assert result.loc[0, "name"] == "John Doe"
    assert result.loc[0, "email"] == "john@example.com"

