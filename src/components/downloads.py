from datetime import datetime

import pandas as pd
import polars as pl
import streamlit as st


def render_download_buttons(df_filtrado: pl.DataFrame, df_matriz: pd.DataFrame):
    """
    Renderiza los botones de descarga de datos.

    Args:
        df_filtrado: DataFrame filtrado de Polars
        df_matriz: DataFrame de pandas con la matriz pivoteada
    """
    st.markdown("### 📥 Descargar Datos")
    col1, col2 = st.columns(2)

    with col1:
        csv = df_filtrado.write_csv()
        st.download_button(
            label="⬇️ Descargar datos filtrados (CSV)",
            data=csv,
            file_name=f"datos_filtrados_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv",
        )

    with col2:
        csv_matriz = df_matriz.to_csv(index=True)
        st.download_button(
            label="⬇️ Descargar matriz (CSV)",
            data=csv_matriz,
            file_name=f"matriz_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv",
        )
