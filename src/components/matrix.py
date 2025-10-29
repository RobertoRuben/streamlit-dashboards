"""Componente para mostrar la matriz de evaluación."""

import polars as pl
import streamlit as st


def render_evaluation_matrix(df_filtrado: pl.DataFrame):
    """
    Renderiza la matriz de evaluación estilo Power BI.

    Args:
        df_filtrado: DataFrame filtrado de Polars

    Returns:
        DataFrame de pandas con la matriz pivoteada para otros componentes
    """
    st.subheader("📊 Matriz de Evaluación")

    matriz_data = df_filtrado.group_by(["Variable", "Lote"]).agg(
        [pl.col("Valor").mean().alias("Promedio")]
    )

    matriz_pivot = matriz_data.pivot(
        values="Promedio", index="Variable", on="Lote"
    ).sort("Variable")

    valor_cols = [col for col in matriz_pivot.columns if col != "Variable"]

    if valor_cols:
        matriz_pivot = matriz_pivot.with_columns(
            [pl.concat_list([pl.col(c) for c in valor_cols]).list.mean().alias("Total")]
        )

    df_display = matriz_pivot.to_pandas()

    numeric_cols = df_display.select_dtypes(include=["float64", "float32"]).columns
    df_display[numeric_cols] = df_display[numeric_cols].round(2)

    st.markdown(
        """
        <style>
        .dataframe thead tr th {
            background-color: #a91f24 !important;
            color: white !important;
            font-weight: bold !important;
            text-align: center !important;
            font-size: 12px !important;
            padding: 8px !important;
        }
        .dataframe tbody tr td {
            text-align: center !important;
            font-size: 11px !important;
            padding: 6px !important;
        }
        </style>
    """,
        unsafe_allow_html=True,
    )

    st.dataframe(
        df_display,
        width="stretch",
        height=600,
    )

    return df_display
