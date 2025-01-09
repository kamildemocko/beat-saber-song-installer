from pathlib import Path
import zipfile

from steam_folders import SteamFolders

class Copier:
    def __init__(self, steam: SteamFolders) -> None:
        self.steam = steam

    def copy_to_game(self, map_path: Path) -> None:
        map_name = map_path.stem
        beatsaber_folder: Path = self.steam.find_game_folder("Beat Saber")

        copy_to_folder = beatsaber_folder.joinpath(rf"Beat Saber_Data\CustomLevels\{map_name}")
        if copy_to_folder.exists():
            raise ValueError(f"map {map_name} already exists")
        
        copy_to_folder.mkdir()
        with zipfile.ZipFile(map_path, "r") as zip:
            zip.extractall(copy_to_folder)
