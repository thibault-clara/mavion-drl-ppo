# Configuration file for the Sphinx documentation builder.

# -- Path setup --------------------------------------------------------------

import os
import sys

# Adjust this so it points to your package root from docs/source/
sys.path.insert(0, os.path.abspath("../.."))

# -- Project information -----------------------------------------------------

project = "mavion-drl-ppo"
author = "Vicente ACOSTA and Thibault CLARA"
copyright = "2026, Vicente ACOSTA and Thibault CLARA"
release = "v1.0"

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx_rtd_theme",
    "sphinx.ext.mathjax",
    "sphinx.ext.autodoc",
]

templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"

html_static_path = ["_static"]

html_theme_options = {
    "navigation_depth": -1,
    "collapse_navigation": False,
}