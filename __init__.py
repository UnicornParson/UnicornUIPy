from .UnicornUIGlobal import *
from .windowinfo import WindowInfo
from .appskin import *
from .UnicornUIGlobal import *
from .console_controller import *
from PyQt6.QtCore import QObject, pyqtProperty, pyqtEnum
from PyQt6.QtQml import qmlRegisterSingletonType,  QQmlEngine, QJSEngine
from enum import Enum


class ButtonState(Enum):
    Normal = 0
    Disabled = 1
    Active = 2
    Hovered = 3

class ButtonStateObject(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._colors = ButtonState

    @pyqtProperty(int, constant=True)
    def Normal(self):
        return self._colors.Normal.value
    @pyqtProperty(int, constant=True)
    def Disabled(self):
        return self._colors.Disabled.value 
    @pyqtProperty(int, constant=True)
    def Active(self):
        return self._colors.Active.value 
    @pyqtProperty(int, constant=True)
    def Hovered(self):
        return self._colors.Hovered.value 
    
def my_color_singleton_factory(engine: QQmlEngine, extension: QJSEngine):
    return ButtonStateObject()

class TemplatesTypes(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

    @staticmethod
    def register_types():
        # Register ButtonState as a singleton in QML
        qmlRegisterSingletonType(
            ButtonStateObject,
            "TemplatesTypes",  # Namespace (URI) for your application
            1,                 # Major version
            0,                 # Minor version
            my_color_singleton_factory, 
            "ButtonState"     # Name under which it will be accessible in QML
        )
__all__ = ["WindowInfo", "ButtonState",
            "TemplatesTypes", "Skin", "UnicornUIGlobal",
            "QmlLogWrapper", "ConsoleController"] 
