from pathlib import Path
import pandas as pd


def load_users(df: pd.DataFrame, output_path: str | Path) -> None:
    """Salva os dados transformados em um novo arquivo CSV."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False, encoding="utf-8-sig")
