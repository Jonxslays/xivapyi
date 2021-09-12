import re

from xivapyi import __author__, __license__, __maintainer__, __url__, __version__


def test_metadata() -> None:
    with open("pyproject.toml", "r") as f:
        meta = f.read()

        ver = re.search(r"version = \"(.*)\"", meta)
        author = re.search(r"authors = \[\"(.*)\"\]", meta)
        license = re.search(r"license = \"(.*)\"", meta)
        url = re.search(r"repository = \"(.*)\"", meta)

    if not ver or not author or not license or not url:
        raise LookupError("Unable to find metadata in pyproject.toml")

    assert author.group(1) == __author__
    assert author.group(1) == __maintainer__
    assert license.group(1) == __license__
    assert url.group(1) == __url__
    assert ver.group(1) == __version__
