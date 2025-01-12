import platform
import argparse


def init() -> list[str]:
    if platform.system() != "Windows":
        raise SystemError("only Windows system supported!")

    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="the map zip path")

    return parser.parse_args()
