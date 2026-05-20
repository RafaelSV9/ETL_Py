from pathlib import Path
import pandas as pd


def extract_users(csv_path: str | Path) -> pd.DataFrame:
    """Lê os usuários a partir de um arquivo CSV."""
    csv_path = Path(csv_path)

    if not csv_path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {csv_path}")

    df = pd.read_csv(csv_path)

    required_columns = {"id", "nome", "conta", "cartao", "segmento"}
    missing_columns = required_columns - set(df.columns)

    if missing_columns:
        raise ValueError(f"Colunas obrigatórias ausentes: {missing_columns}")

    return df
