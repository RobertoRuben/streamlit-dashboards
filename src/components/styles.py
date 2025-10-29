import streamlit as st


def apply_custom_styles():
    st.markdown(
        """
        <style>
        /* Estilos generales */
        .main {
            padding: 1rem;
        }
        
        .stPlotlyChart {
            width: 100%;
        }
        
        /* Ocultar solo el menú hamburguesa (MainMenu) */
        #MainMenu {
            visibility: hidden;
        }
        
        /* Ocultar el footer "Made with Streamlit" */
        footer {
            visibility: hidden;
        }
        
        /* Responsive para móviles */
        @media (max-width: 768px) {
            .row-widget.stMultiSelect {
                width: 100%;
            }
        }
        </style>
    """,
        unsafe_allow_html=True,
    )
