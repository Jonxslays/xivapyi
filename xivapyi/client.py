import asyncio
import atexit
import typing as t

from aiohttp import ClientSession

__all__: t.List[str] = [
    "Client",
]


class Client:
    """Async client with helper methods for making calls to the XIVAPI.

    Args:
        token: str
            The XIVAPI api key to use for requests.
        session: Optional[aiohttp.ClientSession]
            The Client Session to use for requests. Defaults to
            None. If no Client Session is passed, one will be
            created for you.
    """

    __slots__: t.Sequence[str] = ("_loop", "_url", "_session", "_token")

    def __init__(self, token: str, *, session: t.Optional[ClientSession] = None) -> None:
        self._loop = asyncio.get_event_loop()
        self._token = token
        self._url = "https://xivapi.com"

        if isinstance(session, ClientSession):
            self._session = session
        else:
            self._session = ClientSession()
            atexit.register(self.close)

    @property
    def session(self) -> ClientSession:
        """The Client Session used for web requests."""
        if self._session.closed:
            self._session = ClientSession()

        return self._session

    @property
    def url(self) -> str:
        """The base url for the XIVAPI."""
        return self._url

    def close(self) -> None:
        """Closes down the in use Client Session.

        This function is scheduled to run automatically on program
        exit if no Client Session is passed during the Client
        instantiation (It can be called manually as well). If an
        external Client Session is passed however, this function will
        not be scheduled to preserve the integrity of your existing
        Client Session.
        """
        if isinstance(self._session, ClientSession):
            if not self._session.closed:
                self._loop.run_until_complete(self._session.close())
