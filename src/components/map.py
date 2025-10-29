"""Componente para mostrar el mapa de distribución geográfica."""

import plotly.express as px
import polars as pl
import streamlit as st


def render_geographic_map(df_filtrado: pl.DataFrame):
    """
    Renderiza el mapa de distribución geográfica con Plotly.

    Args:
        df_filtrado: DataFrame filtrado de Polars
    """
    st.subheader("🗺️ Distribución Geográfica")

    df_mapa = df_filtrado.filter(
        pl.col("Latitud").is_not_null() & pl.col("Longitud").is_not_null()
    )

    if len(df_mapa) > 0:
        df_mapa_pd = df_mapa.to_pandas()

        fig = px.scatter_map(
            df_mapa_pd,
            lat="Latitud",
            lon="Longitud",
            color="Evaluador", 
            hover_data={
                "Evaluador": True,
                "Lote": True,
                "Variable": True,
                "Valor": ":.2f",  
                "Latitud": False,  
                "Longitud": False,  
            },
            zoom=13,
            height=600,
            title="Ubicación de Evaluaciones por Evaluador",
        )

        fig.update_layout(
            margin={"r": 0, "t": 40, "l": 0, "b": 0},
            legend=dict(
                orientation="v",
                yanchor="top",
                y=0.99,
                xanchor="left",
                x=0.01,
                bgcolor="rgba(255, 255, 255, 0.95)",  
                bordercolor="rgba(0, 0, 0, 0.3)",  
                borderwidth=2,
                font=dict(
                    size=12,
                    color="black",  
                    family="Arial, sans-serif",
                ),
                title=dict(
                    text="<b>Evaluadores</b>", 
                    font=dict(size=14, color="black"),
                ),
            ),
        )

        st.plotly_chart(
            fig,
            use_column_width=True,
            config={
                "displayModeBar": True,
                "displaylogo": False,
                "modeBarButtonsToRemove": ["lasso2d", "select2d"],
            },
        )

    else:
        st.info(
            "ℹ️ No hay datos de geolocalización para mostrar con los filtros seleccionados."
        )
