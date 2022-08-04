"""Balanced diversity solver xoxo to the square."""
import os
from typing import List

APP_NAME = 'Balanced diversity solver xoxo to the square.'
APP_ALIAS = 'xoxo'
APP_ENV = 'XOXO'
DEBUG = bool(os.getenv(f'{APP_ENV}_DEBUG', ''))
VERBOSE = bool(os.getenv(f'{APP_ENV}_VERBOSE', ''))
QUIET = False
STRICT = bool(os.getenv(f'{APP_ENV}_STRICT', ''))
ENCODING = 'utf-8'
ENCODING_ERRORS_POLICY = 'ignore'
DEFAULT_CONFIG_NAME = '.xoxo.json'
DEFAULT_LF_ONLY = 'YES'

# [[[fill git_describe()]]]
__version__ = '2022.8.4+parent.c7f09ef7'
# [[[end]]] (checksum: 18b2041736060202db7f90641d05489e)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)
__all__: List[str] = []
