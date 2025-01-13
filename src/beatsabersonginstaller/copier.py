from pathlib import Path
import zipfile

from steam_folders import SteamFolders

class CopyError(Exception):
    ...

class Copier:
    def __init__(self, steam: SteamFolders) -> None:
        self.steam = steam

    def copy_to_game(self, map_path: Path, delete_map: bool) -> None:
        map_name = map_path.stem

        if not zipfile.is_zipfile(map_path):
            raise CopyError(f"map {map_name} is not a valid map!")

        beatsaber_folder: Path = self.steam.find_game_folder("Beat Saber")

        copy_to_folder = beatsaber_folder.joinpath(rf"Beat Saber_Data\CustomLevels\{map_name}")
        if copy_to_folder.exists():
            raise CopyError(f"map {map_name} is already installed!")
        
        copy_to_folder.mkdir()
        with zipfile.ZipFile(map_path, "r") as file:
            file.extractall(copy_to_folder)
        
        if delete_map:
            map_path.unlink()
