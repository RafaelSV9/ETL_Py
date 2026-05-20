from pathlib import Path

from extract import extract_users
from transform import transform_users
from load import load_users


BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = BASE_DIR / "data" / "usuarios.csv"
OUTPUT_FILE = BASE_DIR / "data" / "usuarios_transformados.csv"


def run_pipeline() -> None:
    print("Iniciando pipeline ETL...")

    users_df = extract_users(INPUT_FILE)
    print(f"Extração concluída: {len(users_df)} usuários encontrados.")

    transformed_df = transform_users(users_df)
    print("Transformação concluída: mensagens personalizadas geradas.")

    load_users(transformed_df, OUTPUT_FILE)
    print(f"Carregamento concluído: arquivo salvo em {OUTPUT_FILE}")


if __name__ == "__main__":
    run_pipeline()
