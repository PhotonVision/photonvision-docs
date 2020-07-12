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

project = 'PhotonVision'
copyright = '2020, PhotonVision'
author = 'Banks Troutman, Matt Morley'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
	"sphinx_rtd_theme",
	'sphinx.ext.autosectionlabel',
	'sphinx_tabs.tabs',
	"sphinxext.opengraph",
	"sphinxcontrib.ghcontributors"
]

# Configure OpenGraph support

ogp_site_url = "https://docs.photonvision.org/en/latest/"
ogp_site_name = "PhotonVision Documentation"
ogp_image = "https://raw.githubusercontent.com/PhotonVision/photonvision-docs/master/source/assets/RectLogo.png"

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# Enable hover content on glossary term
hoverxref_roles = ['term']

# Autosection labels prefix document path and filename
autosectionlabel_prefix_document = True

# -- Options for HTML output -------------------------------------------------

html_title = "PhotonVision Docs"

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme = 'sphinx_material'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# html_context  = { 'css_files': [ 'theme_overrides.css' ] }

html_favicon = 'assets/RoundLogo.png'
html_logo = 'assets/RectLogo.png'

html_theme_options = {
	'base_url': 'https://docs.photonvision.org/',
	'repo_url': 'https://github.com/PhotonVision/photonvision',
	'theme_color': '#006492',
	'color_primary': '#006492',
	'color_accent': 'yellow',
	'repo_name': 'PhotonVision',
	'globaltoc_depth': 2,
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Applying the css stylesheet.
def setup(app):
	app.add_css_file('css/pv-rtd.css')

suppress_warnings = ['epub.unknown_project_files']

sphinx_tabs_valid_builders = ['epub', 'linkcheck']
