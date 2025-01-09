import argparse
from pathlib import Path

from steam_folders import SteamFolders
from copier import Copier


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="the map zip path")

    args = parser.parse_args()

    print("Preparing to copy")

    map_path = Path(args.path)
    steam = SteamFolders()

    print("Copying")

    copier = Copier(steam)
    copier.copy_to_game(map_path)

    input("Done")


if __name__ == "__main__":
    run()
