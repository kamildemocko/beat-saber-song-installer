from pathlib import Path

from init import init
from steam_folders import SteamFolders
from  copier import Copier, CopyError
from gui import Window


if __name__ == "__main__":
    # args = init()
    steam = SteamFolders()
    copier = Copier(steam)
    window = Window(copier.copy_to_game)

    # map_path = Path(args.path)

    # copier.copy_to_game(map_path, args.delete)

    window.mainloop()

    # try:
    #     run()

    # except CopyError as ex:
    #     print(f"error: {ex}")

    # input("Done\n\nEnter to exit")
