from typing import Callable
from pathlib import Path
import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES

from copier import CopyError
from steam_folders import SteamFolderError

class Window(TkinterDnD.Tk):
    def __init__(self, drop_callback: Callable):
        self._callable = drop_callback

        super().__init__()
        self.title("BeatSaber Song Installer")
        self.geometry("500x300")

        self.label = tk.Label(self, text="Drag & Drop the BeatSaber map here", font=("Arial", 16))
        self.label.pack(expand=True, fill=tk.BOTH, anchor=tk.CENTER)

        self.status = tk.Text(self, height=6)
        self.status.configure(state="disabled")
        self.status.pack(anchor=tk.S)

        self.drop_target_register(DND_FILES)
        self.dnd_bind("<<Drop>>", self.on_file_drop)

    
    def on_file_drop(self, event: tk.Event) -> None:
        path = Path(event.data.strip("{}")).resolve()

        try:
            self.status.configure(state="normal")

            self._callable(path, False)

            self.status.insert("1.0", "done...\n")

        except (CopyError, SteamFolderError) as exc:
            self.status.insert("1.0", f"{exc}\n")
        
        finally:
            self.status.configure(state="disabled")
