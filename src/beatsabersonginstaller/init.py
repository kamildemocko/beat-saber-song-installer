import platform


def initialize() -> None:
    if platform.system() != "Windows":
        raise SystemError("only Windows system supported!")
