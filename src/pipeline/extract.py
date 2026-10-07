from pathlib import Path

import pandas as pd


def extract_customers(file_path: str | Path) -> pd.DataFrame:
    """
    Load customer data from a CSV file.

    Args:
        file_path: Path to the CSV file.

    Returns:
        A DataFrame containing the customer data.

    Raises:
        FileNotFoundError: If the CSV file does not exist.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    return pd.read_csv(path)