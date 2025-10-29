"""Componente para mostrar el logo en el sidebar."""

from pathlib import Path

import streamlit as st


def render_sidebar_logo():
    """
    Renderiza el logo de Danper en el sidebar con autoadaptación responsive.
    El logo se adapta al ancho del sidebar sin perder calidad.
    """
    # Obtener la ruta del logo
    logo_path = Path(__file__).parent.parent / "public" / "danper-logo.png"

    if logo_path.exists():
        # Aplicar estilos CSS para responsive y centrado
        st.sidebar.markdown(
            """
            <style>
            /* Centrar el contenedor de la imagen */
            div[data-testid="stSidebar"] [data-testid="stImage"] {
                display: flex;
                justify-content: center;
                align-items: center;
            }
            
            /* Imagen responsive - máximo 90% del ancho del sidebar */
            div[data-testid="stSidebar"] [data-testid="stImage"] img {
                max-width: 90%;
                height: auto;
                margin: 0.5rem 0;
                object-fit: contain;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

        # Usar width='stretch' para que se adapte al ancho disponible
        # El ancho máximo será el del sidebar (aproximadamente 260px)
        st.sidebar.image(
            str(logo_path),
            width="stretch",
        )
        st.sidebar.markdown("---")
    else:
        st.sidebar.warning("⚠️ Logo no encontrado")
