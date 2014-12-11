# -*- coding: utf-8 -*-
#
import sys
import os

# GENERAL CONFIGURATION
# --------------------------------------
source_encoding  = 'utf-8-sig'
source_suffix    = '.rst'
master_doc       = 'index'
exclude_patterns = ['_build']
pygments_style   = 'sphinx'

# PROJECT INFORMATION
# --------------------------------------
project   = u'Voces Nuestras, Guía de uso'
copyright = u'2014, Asociación Voces Nuestras'
version   = '1'
release   = '1'
language  = 'es'

# HTML OUTPUT
# --------------------------------------
html_title = "Voces Nuestras, Guia de Uso"
html_logo    = 'img/logo.svg'
html_favicon = 'img/favicon.ico'
html_theme = "default"
html_theme_options = {
  "headfont": "'Lato', sans-serif",
  "bodyfont": "'Lato', sans-serif",
  "bgcolor":          "#f7f7f7",
  "textcolor":        "#222",
  "linkcolor":        "#5094c5",
  "visitedlinkcolor": "#5094c5",
  "headbgcolor":      "#f7f7f7",
  "headtextcolor":    "#222",
  "headlinkcolor":    "#5094c5",
  "relbarbgcolor":    "#f6b32a",
  "relbartextcolor":  "#222",
  "relbarlinkcolor":  "#222",
  "sidebarbgcolor":   "#f7f7f7",
  "sidebartextcolor": "#222",
  "sidebarlinkcolor": "f6902f",
  "footerbgcolor":    "#f6b32a",
  "footertextcolor":  "#222"
}
htmlhelp_basename = 'VocesNuestrasdoc'
# html_show_sourcelink = False
# html_show_copyright  = False
# html_show_sphinx     = False

# LATEX OUTPUT
# --------------------------------------
latex_documents = [
  ('index', 'VocesNuestras.tex', u'Voces Nuestras, Guía de uso',
    u'Asociación Voces Nuestras', 'manual'),
]

# MAN PAGE OUTPUT
# --------------------------------------
man_pages = [
  ('index', 'vocesnuestras', u'Voces Nuestras, Guía de uso',
    [u'Asociación Voces Nuestras'], 1)
]

# TEXINFO OUTPUT
# --------------------------------------
texinfo_documents = [
  ('index', 'VocesNuestras', u'Voces Nuestras, Guía de uso',
    u'Asociación Voces Nuestras', 'VocesNuestras',
    'Voces Nuestras, Guía de uso.', 'manual'),
]

# EPUB OUTPUT
# --------------------------------------
epub_title     = u'Voces Nuestras'
epub_author    = u'Asociación Voces Nuestras'
epub_publisher = u'Asociación Voces Nuestras'
epub_copyright = u'2014, Asociación Voces Nuestras'
epub_exclude_files = ['search.html']
