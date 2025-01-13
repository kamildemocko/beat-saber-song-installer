from typing import Callable
from datetime import datetime as dt
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
        self._delete = tk.IntVar()

        self.label = tk.Label(self, text="Drag & Drop the BeatSaber map here", font=("Arial", 16))
        self.label.pack(expand=True, fill=tk.BOTH, anchor=tk.CENTER)

        self.delete = tk.Checkbutton(self, text="Delete file after import", variable=self._delete)
        self.delete.pack(anchor=tk.W, padx=15, pady=10)

        self.status = tk.Text(self, height=6)
        self.status.configure(state="disabled")
        self.status.pack(anchor=tk.S)

        self.drop_target_register(DND_FILES)
        self.dnd_bind("<<Drop>>", self.on_file_drop)

    
    def on_file_drop(self, event: tk.Event) -> None:
        path = Path(event.data.strip("{}")).resolve()

        try:
            self.status.configure(state="normal")
            self._callable(path, True if self._delete.get() else False)
            self.status.insert("1.0", f"{self._get_time()} Map imported!\n")

        except (CopyError, SteamFolderError) as exc:
            self.status.insert("1.0", f"{self._get_time()} {exc}\n")

        except Exception as exc:
            self.status.insert("1.0", f"{self._get_time()} SYSERR: {exc}\n")
        
        finally:
            self.status.configure(state="disabled")
    
    @staticmethod
    def _get_time() -> str:
        return dt.now().time().strftime("%H:%M:%S")
