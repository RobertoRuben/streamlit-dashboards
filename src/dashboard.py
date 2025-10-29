import streamlit as st

from components import (
    apply_custom_styles,
    load_data,
    render_data_table,
    render_download_buttons,
    render_evaluation_matrix,
    render_filters,
    render_geographic_map,
    render_metrics,
    render_sidebar_logo,
)
from config import PAGE_CONFIG
from database import engine

st.set_page_config(**PAGE_CONFIG)

apply_custom_styles()

render_sidebar_logo()

st.title("📊 Conteos")
st.markdown("---")

with st.spinner("Cargando datos..."):
    try:
        df = load_data(engine)
        if df is None or len(df) == 0:
            st.error("❌ No hay datos para procesar")
            st.stop()
        st.success(f"✅ Datos cargados: {len(df):,} registros")
    except Exception as e:
        st.error(f"Error al cargar datos: {str(e)}")
        import traceback

        st.code(traceback.format_exc())
        st.stop()

df_filtrado = render_filters(df)

render_metrics(df, df_filtrado)

st.markdown("---")

if len(df_filtrado) > 0:
    df_matriz = render_evaluation_matrix(df_filtrado)

    render_geographic_map(df_filtrado)

    st.markdown("---")

    render_download_buttons(df_filtrado, df_matriz)

    render_data_table(df_filtrado)

else:
    st.warning("⚠️ No hay datos para mostrar con los filtros seleccionados.")
    st.info("💡 Intenta ajustar los filtros para ver más resultados.")

st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>@Danper 2025</div>",
    unsafe_allow_html=True,
)
