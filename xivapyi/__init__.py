import typing

from . import errors
from .client import Client

__all__: typing.List[str] = [
    "Client",
    "errors",
    "__version__",
    "__author__",
    "__maintainer__",
    "__license__",
    "__url__",
]

__version__: str = "0.1.1"
__author__: str = "Jonxslays"
__maintainer__: str = "Jonxslays"
__license__: str = "BSD-3-Clause"
__url__: str = "https://github.com/Jonxslays/xivapyi"
