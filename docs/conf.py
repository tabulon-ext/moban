# -*- coding: utf-8 -*-
DESCRIPTION = (
    'General purpose static text generator' +
    ''
)
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'moban'
copyright = '2017-2020 Onni Software Ltd.'
author = 'C. W.'
# The short X.Y version
version = '0.8.2'
# The full version, including alpha/beta/rc tags
release = '0.8.2'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [    'sphinx.ext.autodoc',    'sphinx.ext.doctest',    'sphinx.ext.intersphinx',    'sphinx.ext.viewcode',]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Extension configuration -------------------------------------------------
# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/3/': None}
# TODO: html_theme not configurable upstream
html_theme = 'default'

# TODO: DESCRIPTION not configurable upstream
texinfo_documents = [
    ('index', 'moban',
     'moban Documentation',
     'Onni Software Ltd.', 'moban',
     DESCRIPTION,
     'Miscellaneous'),
]
intersphinx_mapping.update({
})
master_doc = "index"
