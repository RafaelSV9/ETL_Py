import pandas as pd


def generate_marketing_message(nome: str, cartao: str, segmento: str) -> str:
    """Gera uma mensagem personalizada simulando uma etapa de IA."""
    return (
        f"Olá {nome}, analisamos seu perfil no segmento {segmento} e identificamos "
        f"benefícios exclusivos para o seu cartão {cartao}. Aproveite as oportunidades "
        "disponíveis para organizar melhor sua vida financeira."
    )


def transform_users(df: pd.DataFrame) -> pd.DataFrame:
    """Transforma os dados criando mensagens personalizadas."""
    transformed_df = df.copy()

    transformed_df["mensagem"] = transformed_df.apply(
        lambda row: generate_marketing_message(
            nome=row["nome"],
            cartao=row["cartao"],
            segmento=row["segmento"],
        ),
        axis=1,
    )

    return transformed_df
