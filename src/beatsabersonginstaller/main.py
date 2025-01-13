from pathlib import Path

from init import init
from steam_folders import SteamFolders
from  copier import Copier


def run():
    args = init()

    print("Preparing to copy")

    map_path = Path(args.path)
    steam = SteamFolders()

    print("Copying")

    copier = Copier(steam)
    copier.copy_to_game(map_path)

    input("Done")


if __name__ == "__main__":
    run()
