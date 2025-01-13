from init import initialize
from steam_folders import SteamFolders
from  copier import Copier
from gui import Window


if __name__ == "__main__":
    initialize()
    steam = SteamFolders()
    copier = Copier(steam)
    window = Window(copier.copy_to_game)

    window.mainloop()
