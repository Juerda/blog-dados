#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Pelican configuration file for Jordan Arruda's personal blog.

This configuration file follows Clean Code principles and security best practices.
It's organized into logical sections for better maintainability.

Author: Jordan Arruda
License: MIT
Last Updated: December 2025
"""

import os
from typing import Dict, List

# =============================================================================
# SITE METADATA & IDENTITY
# =============================================================================

# Core site information
AUTHOR: str = 'Jordan Arruda'
SITENAME: str = 'Jordan Arruda'
SITESUBTITLE: str = 'Dados, Análises e Insights'
SITEDESCRIPTION: str = 'Blog pessoal de Jordan Arruda sobre análise de dados, Python e tecnologia. Compartilhando conhecimento e insights sobre ciência de dados.'

# URL Configuration (empty for development, set by Vercel in production)
SITEURL: str = os.environ.get('SITE_URL', '')

# Localization
TIMEZONE: str = 'America/Sao_Paulo'
DEFAULT_LANG: str = 'pt_BR'
DEFAULT_DATE_FORMAT: str = '%d de %B de %Y'

# =============================================================================
# URL STRUCTURE & ROUTING
# =============================================================================

# Article URLs (SEO-friendly structure)
ARTICLE_URL: str = 'posts/{slug}/'
ARTICLE_SAVE_AS: str = 'posts/{slug}/index.html'

# Page URLs (clean URLs without .html)
PAGE_URL: str = '{slug}/'
PAGE_SAVE_AS: str = '{slug}/index.html'

# Homepage
INDEX_SAVE_AS: str = 'index.html'

# Blog archive page
ARCHIVES_SAVE_AS: str = 'blog.html'

# =============================================================================
# DIRECTORY STRUCTURE & PATHS
# =============================================================================

# Content and output directories
PATH: str = 'content'
OUTPUT_PATH: str = 'output/'

# Static files configuration
STATIC_PATHS: List[str] = ['images']

# Extra path metadata for theme assets
EXTRA_PATH_METADATA: Dict[str, Dict[str, str]] = {
    'theme/static/css': {'path': 'theme/css'},
    'theme/static/js': {'path': 'theme/js'},
    'theme/static/images': {'path': 'theme/images'},
}

# =============================================================================
# THEME & APPEARANCE
# =============================================================================

# Theme configuration
THEME: str = 'theme'

# Template generation
DIRECT_TEMPLATES: List[str] = ['index', 'tags', 'categories', 'archives']
PAGINATED_TEMPLATES: Dict = {}

# Menu display settings (using custom navigation)
DISPLAY_PAGES_ON_MENU: bool = False
DISPLAY_CATEGORIES_ON_MENU: bool = False
DISPLAY_RECENT_POSTS_ON_MENU: bool = False

# =============================================================================
# CONTENT ORDERING & PAGINATION
# =============================================================================

# Sort articles by date (newest first)
ARTICLE_ORDER_BY: str = 'date'
REVERSE_ARTICLE_ORDER: bool = True

# Disable pagination (show all articles)
DEFAULT_PAGINATION: bool = False

# =============================================================================
# PLUGINS & EXTENSIONS
# =============================================================================

PLUGIN_PATHS: List[str] = ['plugins']
PLUGINS: List = []  # Add plugins here as needed

# =============================================================================
# RSS/ATOM FEEDS
# =============================================================================

# Main feed (all content)
FEED_ALL_ATOM: str = 'feeds/all.atom.xml'

# Category-specific feeds
CATEGORY_FEED_ATOM: str = 'feeds/{slug}.atom.xml'

# Disable translation feeds (single language blog)
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# =============================================================================
# PERFORMANCE & CACHING
# =============================================================================

# Disable content cache for development (enable in production if needed)
LOAD_CONTENT_CACHE: bool = False

# =============================================================================
# SECURITY & BEST PRACTICES
# =============================================================================

# Relative URLs for development (Vercel will use absolute URLs in production)
RELATIVE_URLS: bool = not bool(SITEURL)

# Delete output directory before building (ensures clean builds)
DELETE_OUTPUT_DIRECTORY: bool = False

# =============================================================================
# SOCIAL & EXTERNAL LINKS
# =============================================================================

SOCIAL: List[tuple] = [
    ('GitHub', 'https://github.com/Juerda'),
    ('LinkedIn', 'https://www.linkedin.com/in/jordanarruda/'),
    ('Twitter', 'https://twitter.com/jordandearruda'),
]

# =============================================================================
# SEO & METADATA
# =============================================================================

# Site author for SEO
SITEAUTHOR: str = AUTHOR

# Copyright notice
COPYRIGHT_YEAR: str = '2025'
COPYRIGHT_NAME: str = AUTHOR
