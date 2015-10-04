# -*- coding: utf-8 -*-
extensions = ['sphinxcontrib.ros', 'sphinx.ext.intersphinx']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'sample'
copyright = u'2015, otamachan'
author = u'otamachan'
version = '0.1.0'
release = '0.1.0'
language = 'ja'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
html_theme = 'classic'
html_static_path = []
intersphinx_mapping = {'ros':
  ('http://otamachan.github.io/sphinxros/indigo/', None)}
