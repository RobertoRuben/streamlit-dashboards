import polars as pl
import streamlit as st


def render_filters(df: pl.DataFrame) -> pl.DataFrame:
    """
    Renderiza los filtros en el sidebar y devuelve el DataFrame filtrado.

    Args:
        df: DataFrame original de Polars

    Returns:
        DataFrame filtrado según las selecciones del usuario
    """
    st.sidebar.header("🔍 Filtros")

    df_temp = df.clone()

    fundos = sorted(df_temp["Fundo"].unique().to_list())
    fundo_seleccionado = st.sidebar.multiselect("Fundo", options=fundos, default=[])
    if fundo_seleccionado:
        df_temp = df_temp.filter(pl.col("Fundo").is_in(fundo_seleccionado))

    modulos = sorted(df_temp["Modulo"].unique().to_list())
    modulo_seleccionado = st.sidebar.multiselect("Módulo", options=modulos, default=[])
    if modulo_seleccionado:
        df_temp = df_temp.filter(pl.col("Modulo").is_in(modulo_seleccionado))

    turnos = sorted(df_temp["Turno"].unique().to_list())
    turno_seleccionado = st.sidebar.multiselect("Turno", options=turnos, default=[])
    if turno_seleccionado:
        df_temp = df_temp.filter(pl.col("Turno").is_in(turno_seleccionado))

    evaluadores = sorted(df_temp["Evaluador"].unique().to_list())
    evaluador_seleccionado = st.sidebar.multiselect(
        "Evaluador", options=evaluadores, default=[]
    )
    if evaluador_seleccionado:
        df_temp = df_temp.filter(pl.col("Evaluador").is_in(evaluador_seleccionado))

    cartillas = sorted(df_temp["Cartilla"].unique().to_list())
    cartilla_seleccionada = st.sidebar.multiselect(
        "Cartilla", options=cartillas, default=[]
    )
    if cartilla_seleccionada:
        df_temp = df_temp.filter(pl.col("Cartilla").is_in(cartilla_seleccionada))

    semanas = sorted(df_temp["Semana"].unique().to_list())
    semana_seleccionada = st.sidebar.multiselect(
        "Semana del Año", options=semanas, default=[]
    )
    if semana_seleccionada:
        df_temp = df_temp.filter(pl.col("Semana").is_in(semana_seleccionada))

    min_fecha = df_temp["Fecha"].min()
    max_fecha = df_temp["Fecha"].max()

    fecha_inicio = st.sidebar.date_input(
        "Fecha Inicio", value=min_fecha, min_value=min_fecha, max_value=max_fecha
    )

    fecha_fin = st.sidebar.date_input(
        "Fecha Fin", value=max_fecha, min_value=min_fecha, max_value=max_fecha
    )

    df_temp = df_temp.filter(
        (pl.col("Fecha") >= fecha_inicio) & (pl.col("Fecha") <= fecha_fin)
    )

    if st.sidebar.button("🔄 Limpiar Filtros"):
        st.rerun()

    return df_temp
