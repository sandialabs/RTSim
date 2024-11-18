"""
Configuration file for the Sphinx documentation builder.

Copyright © 2024, National Technology & Engineering Solutions of
Sandia, LLC (NTESS). Under the terms of Contract DE-NA0003525 with
NTESS, the U.S. Government retains certain rights in this software.

This file only contains a selection of the most common options. For a full
list see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html

-- Path setup --------------------------------------------------------------

If extensions (or modules to document with autodoc) are in another directory,
add these directories to sys.path here. If the directory is relative to the
documentation root, use os.path.abspath to make it absolute, like shown here.
"""

import os
import sys

sys.path.insert(0, os.path.abspath(".."))  # noqa: PTH100


# -- Project information -----------------------------------------------------

project = "RTSim"
copyright = """
Copyright © 2024, National Technology & Engineering Solutions of
Sandia, LLC (NTESS). Under the terms of Contract DE-NA0003525 with
NTESS, the U.S. Government retains certain rights in this software.
"""  # noqa: A001
author = "Jason K. Bingham"

# The full version, including alpha/beta/rc tags
import rtsim  # noqa: E402

release = rtsim.__version__


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autosectionlabel",
    "sphinxcontrib.bibtex",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns: list[str] = []

# Bibliography file
bibtex_bibfiles = ["refs.bib"]
bibtex_default_style = "plain"


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
