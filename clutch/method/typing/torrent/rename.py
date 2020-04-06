from typing import Union, Sequence
from typing_extensions import TypedDict, Literal

class TorrentRenameArguments(TypedDict):
    ids: Sequence[Union[str, int]]
    path: str
    name: str


class TorrentRenameResponse(TypedDict):
    path: str
    name: str
    id: int
