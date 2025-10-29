import polars as pl
import streamlit as st
from sqlalchemy import Engine


@st.cache_data(ttl=300)
def load_data(_engine: Engine):
    """
    Carga datos desde PostgreSQL usando Polars.

    Args:
        db_url: URL de conexión a la base de datos PostgreSQL

    Returns:
        DataFrame de Polars con los datos cargados
    """
    sql_query = "SELECT * FROM conteo_consolidado"
    
    df = pl.read_database(
        query=sql_query,
        connection=_engine
    )

    df = df.with_columns(
        [pl.col("Fecha").cast(pl.Date), pl.col("Valor").cast(pl.Float64)]
    )

    df = df.with_columns([pl.col("Fecha").dt.week().alias("Semana")])

    return df
