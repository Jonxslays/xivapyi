import typing

__all__: typing.List[str] = [
    "XivError",
    "FailedRequest",
]


class XivError(Exception):
    """Base exepction, that all xivapyi errors derive from."""

    ...


class FailedRequest(XivError):
    """Raised when a non-ok response is received from XIVAPI."""

    ...
