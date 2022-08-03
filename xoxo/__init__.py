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
__version__ = '2022.8.1+parent.7635e35c'
# [[[end]]] (checksum: 336a0105003ee28994a568480df2fbd9)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)
__all__: List[str] = []
