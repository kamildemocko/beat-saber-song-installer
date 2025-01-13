from typing import Callable
from datetime import datetime as dt
from pathlib import Path
import tkinter as tk
import webbrowser

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

        self._opt_frame()

        self.status = tk.Text(self, height=6)
        self.status.configure(state="disabled")
        self.status.pack(anchor=tk.S)

        self.drop_target_register(DND_FILES)
        self.dnd_bind("<<Drop>>", self.on_file_drop)

    def _opt_frame(self) -> None:
        frame = tk.Frame(self)
        frame.pack(fill=tk.X, padx=20, pady=10)

        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)

        self.delete = tk.Checkbutton(frame, text="Delete map after import", variable=self._delete)
        self.delete.grid(row=0, column=0, sticky=tk.W)
        self.delete.focus()

        self.link = tk.Label(frame, text="GitHub", fg="blue")
        self.link.grid(row=0, column=1, sticky=tk.E)
        self.link.bind(
            "<Button-1>", 
            lambda x: webbrowser.open("https://github.com/kamildemocko/beat-saber-song-installer")
        )

    
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
