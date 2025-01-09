import re
from pathlib import Path
import winreg

class SteamFolders:
    def __init__(self) -> None:
        try:
            hkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\WOW6432Node\Valve\Steam")
        except Exception as exc:
            raise ValueError("cannot find Steam in registry") from exc

        install_path = Path(winreg.QueryValueEx(hkey, "InstallPath")[0])
        if not install_path.exists():
            raise ValueError("cannot find Steam where it's supposted to be")

        self.steamapps_paths: list[Path] = self._get_steamapps_paths(install_path)

    @staticmethod
    def _get_steamapps_paths(root: Path) -> list[Path]:
        config_file = root.joinpath(r"steamapps\libraryfolders.vdf")
        config_file_content = config_file.read_text()

        pattern = re.compile(r'"path"\s+"(.*)"')
        groups = pattern.findall(config_file_content)

        return [Path(g).resolve() for g in groups]

    def find_game_folder(self, name: str) -> Path:
        found: list[Path] = []

        for library in self.steamapps_paths:
            searched_folder = library.joinpath(r"steamapps\common").joinpath(name)
            if searched_folder.exists():
                found.append(searched_folder)

        if len(found) == 0:
            raise ValueError(f"{name} was not found in any library")
        
        if len(found) != 1:
            raise ValueError(f"{name} was found in multiple steamapps libraries")
        
        return found[0]
