from pathlib import Path

from beatsabersonginstaller.init import init
from beatsabersonginstaller.steam_folders import SteamFolders
from  beatsabersonginstaller.copier import Copier


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
