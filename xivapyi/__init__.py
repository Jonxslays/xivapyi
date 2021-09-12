import typing

from . import client
from .client import *

__all__: typing.List[str] = [
    *client.__all__,
]

__version__: str = "0.1.0"
__author__: str = "Jonxslays"
__maintainer__: str = "Jonxslays"
__license__: str = "BSD-3-Clause"
__url__: str = "https://github.com/Jonxslays/xivapyi"
