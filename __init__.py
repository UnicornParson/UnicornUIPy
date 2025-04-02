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

class LedState(Enum):
    Disabled = 0
    On =  1
    Off =  2
    Progress = 3

class LedStateObject(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._states = LedState

    @pyqtProperty(int, constant=True)
    def Disabled(self):
        return self._states.Disabled.value
    @pyqtProperty(int, constant=True)
    def On(self):
        return self._states.On.value 
    @pyqtProperty(int, constant=True)
    def Off(self):
        return self._states.Off.value 
    @pyqtProperty(int, constant=True)
    def Progress(self):
        return self._states.Progress.value 

class ButtonStateObject(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._states = ButtonState

    @pyqtProperty(int, constant=True)
    def Normal(self):
        return self._states.Normal.value
    @pyqtProperty(int, constant=True)
    def Disabled(self):
        return self._states.Disabled.value 
    @pyqtProperty(int, constant=True)
    def Active(self):
        return self._states.Active.value 
    @pyqtProperty(int, constant=True)
    def Hovered(self):
        return self._states.Hovered.value 
    
def button_state_singleton_factory(engine: QQmlEngine, extension: QJSEngine):
    return ButtonStateObject()
def led_state_singleton_factory(engine: QQmlEngine, extension: QJSEngine):
    return LedStateObject()

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
            button_state_singleton_factory, 
            "ButtonState"     # Name under which it will be accessible in QML
        )
        # Register LedState as a singleton in QML
        qmlRegisterSingletonType(
            LedStateObject,
            "TemplatesTypes",  # Namespace (URI) for your application
            1,                 # Major version
            0,                 # Minor version
            led_state_singleton_factory, 
            "LedState"     # Name under which it will be accessible in QML
        )

__all__ = ["WindowInfo", "ButtonState", "LedState",
            "TemplatesTypes", "Skin", "UnicornUIGlobal",
            "QmlLogWrapper", "ConsoleController"] 
