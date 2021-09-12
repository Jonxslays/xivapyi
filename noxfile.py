import nox


def install(session: nox.Session, dev: bool = False) -> nox.Session:
    session.run("poetry", "-q", "shell", external=True)

    if dev:
        session.run("poetry", "install", "-n", external=True)
    else:
        session.run("poetry", "install", "-n", "--no-dev", external=True)

    return session


@nox.session(reuse_venv=True)
def tests(session: nox.Session) -> None:
    session = install(session, True)
    session.run("pytest", "--verbose")


@nox.session(reuse_venv=True)
def types(session: nox.Session) -> None:
    session = install(session, True)
    session.run("mypy", ".", "--strict")


@nox.session(reuse_venv=True)
def formatting(session: nox.Session) -> None:
    session = install(session, True)
    session.run("black", ".", "-l99")
    session.run("len8", "-l", "xivapyi", "tests")


@nox.session(reuse_venv=True)
def imports(session: nox.Session) -> None:
    session = install(session, True)
    session.run(
        "flake8",
        "xivapyi",
        "tests",
        "--select",
        "F4",
        "--extend-ignore",
        "E,F",
        "--extend-exclude",
        "__init__.py,",
    )

    session.run(
        "isort",
        ".",
        "-cq",
        "--profile",
        "black",
        "--skip",
        ".tests",
        "--skip",
        ".venv",
        "--skip",
        ".nox",
    )
