"""Componentes del dashboard."""

from .data_loader import load_data
from .data_table import render_data_table
from .downloads import render_download_buttons
from .filters import render_filters
from .map import render_geographic_map
from .matrix import render_evaluation_matrix
from .metrics import render_metrics
from .sidebar_logo import render_sidebar_logo
from .styles import apply_custom_styles

__all__ = [
    "load_data",
    "render_filters",
    "render_metrics",
    "render_evaluation_matrix",
    "render_geographic_map",
    "render_download_buttons",
    "render_data_table",
    "apply_custom_styles",
    "render_sidebar_logo",
]
