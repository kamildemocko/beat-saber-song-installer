from pathlib import Path

from init import init
from steam_folders import SteamFolders
from  copier import Copier, CopyError


def run():
    args = init()

    map_path = Path(args.path)
    steam = SteamFolders()

    print("Copy")

    copier = Copier(steam)
    copier.copy_to_game(map_path, args.delete)


if __name__ == "__main__":
    print("Prepare")

    try:
        run()

    except CopyError as ex:
        print(f"error: {ex}")

    input("Done\n\nEnter to exit")
