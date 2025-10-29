import polars as pl
import streamlit as st


def render_data_table(df_filtrado: pl.DataFrame):
    """
    Renderiza la tabla expandible con los datos filtrados.

    Args:
        df_filtrado: DataFrame filtrado de Polars
    """
    with st.expander("👁️ Ver datos filtrados"):
        st.dataframe(df_filtrado.to_pandas(), width="stretch", height=400)
