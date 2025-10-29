import polars as pl
import streamlit as st


def render_metrics(df_original: pl.DataFrame, df_filtrado: pl.DataFrame):
    """
    Renderiza las métricas de resumen de registros.

    Args:
        df_original: DataFrame original sin filtros
        df_filtrado: DataFrame filtrado
    """
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Registros", f"{len(df_original):,}")

    with col2:
        st.metric("Registros Filtrados", f"{len(df_filtrado):,}")

    with col3:
        porcentaje = (
            (len(df_filtrado) / len(df_original) * 100) if len(df_original) > 0 else 0
        )
        st.metric("% Filtrado", f"{porcentaje:.1f}%")
