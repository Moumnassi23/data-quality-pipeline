import pandas as pd


def transform_customers(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize customer data.

    - Removes leading/trailing spaces from names and emails.
    - Converts names to title case.
    - Converts emails to lowercase.

    Args:
        df: Input customer DataFrame.

    Returns:
        A transformed copy of the DataFrame.
    """
    result = df.copy()

    result["name"] = result["name"].str.strip().str.title()
    result["email"] = result["email"].str.strip().str.lower()

    return result

