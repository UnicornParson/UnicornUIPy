from PyQt6.QtCore import *
from datetime import datetime
from typing import AnyStr, Optional

class ConsoleController(QObject):
    consoleContentChanged = pyqtSignal(str)

    def __init__(self, parent: QObject | None = None):
        super().__init__(parent)
        self._lines = []
        self.prompt = ">"
        self._fname = None
        
    def setFileOutput(self, fname:str):
        self._fname = fname

    def _save_line(self, line:str):
        if self._fname:
            with open(self._fname, 'a', encoding='utf-8') as f:
                dt = datetime.now().strftime("%d_%m_%Y_%H_%M_%S-%f")
                f.write(f"[{dt}] {line}\n")


    @pyqtProperty(str, notify=consoleContentChanged)
    def text(self):
        txt = ""
        for msg in self._lines:
            txt += f"{self.prompt} {msg}\n"
        return txt
    
    def clearLines(self):
        self._lines = []
        self.consoleContentChanged.emit("")

    def addLine(self, text):
        self._lines.append(text)
        self._save_line(text)
        self.consoleContentChanged.emit("")

    def last(self) -> str:
        return "" if not self._lines else self._lines[-1]

    def update_last(self, text):
        if len(self._lines ) > 0:
            self._lines[-1] = str (text)
        else:
            self._lines.append(text)
        self._save_line(text)
        self.consoleContentChanged.emit("")






