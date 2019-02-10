#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = u'Matheus O. Santos'
SITENAME = u'Matheus O. Santos'
SITEURL= 'https://somatheus.github.io/'

PATH = 'content'
STATIC_PATHS = ['images']

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Theme

THEME = '/home/matheus-os/Downloads/nice-blog-master/'
THEME_COLOR ='cyan'
SIDEBAR_DISPLAY = ['about', 'categories', 'tags']
SIDEBAR_ABOUT = "Jovem de 18 anos apaixonado por programação, formado Técnico em Informática com alguns projetos a fazer."
COPYRIGHT = "Matheus Oliveira Santos 2018"
MY_CURRENT_AGE = datetime.now().year - 1999


# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('github', 'https://github.com/somatheus'),
    ('linkedin', 'https://www.linkedin.com/in/matheus-o-499723142/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
