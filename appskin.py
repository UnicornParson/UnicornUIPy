from PyQt6.QtCore import QObject, pyqtSignal, pyqtProperty
from typing import AnyStr, Optional

class AppSkin(QObject):
    backgroundColorChanged = pyqtSignal(str)
    secondBackgroundColorChanged = pyqtSignal(str)
    mainFontColorChanged = pyqtSignal(str)

    buttonBackgroundColorChanged = pyqtSignal(str)
    buttonFontColorChanged = pyqtSignal(str)
    buttonBorderColorChanged = pyqtSignal(str)

    buttonHoveredBackgroundColorChanged = pyqtSignal(str)
    buttonHoveredFontColorChanged = pyqtSignal(str)
    buttonHoveredBorderColorChanged = pyqtSignal(str)

    buttonDisabledBackgroundColorChanged = pyqtSignal(str)
    buttonDisabledFontColorChanged = pyqtSignal(str)
    buttonDisabledBorderColorChanged = pyqtSignal(str)

    defaultMarginChanged = pyqtSignal(int)
    defaultBorderSizeChanged = pyqtSignal(int)
    defaultBorderRadiusChanged = pyqtSignal(int)

    firstBorderColorChanged = pyqtSignal(str)
    secondBorderColorChanged = pyqtSignal(str)

    def __init__(self, parent: Optional[QObject] = None):
        super().__init__(parent)
        
        """ 
        # Light theme
        self._backgroundColor: str = "#ffffff"
        self._secondBackgroundColor: str = "#f0f0f0"
        self._mainFontColor: str = "#333333"

        self._buttonBackgroundColor: str = "#ffffff"
        self._buttonFontColor: str = "#333333"
        self._buttonBorderColor: str = "#cccccc"

        self._buttonHoveredBackgroundColor: str = "#f0f0f0"
        self._buttonHoveredFontColor: str = "#2196F3"
        self._buttonHoveredBorderColor: str = "#2196F3"

        self._buttonDisabledBackgroundColor: str = "#f8f8f8"
        self._buttonDisabledFontColor: str = "#aaaaaa"
        self._buttonDisabledBorderColor: str = "#cccccc"

        self._firstBorderColor: str = "#cccccc"
        self._secondBorderColor: str = "#999999"
        """
        # Dark+ theme
        self._backgroundColor: str = "#1E1E1E"           # Workspace background
        self._sidebarBackgroundColor: str = "#001F33"   # Sidebar background
        self._foregroundColor: str = "#D4D4D4"         # Main text color
        self._selectionColor: str = "#D7BA7D"          # Text selection color
        self._cursorColor: str = "#AEAFAD"            # Cursor color
        self._insertCursorColor: str = "#FFFFFF"       # Cursor color in insert mode
        self._lineHighlightColor: str = "#0000FF20"    # Line highlight color
        self._activeTabColor: str = "#007ACC"         # Active tab color
        self._inactiveTabColor: str = "#757575"       # Inactive tab color
        self._borderColor: str = "#454545"            # Border color
        self._selectedItemBackgroundColor: str = "#003B71"  # Selected item background color
        self._statusBarBackgroundColor: str = "#001F33"   # Status bar background color



        self._defaultMargin: int = 10
        self._defaultBorderSize: int = 2
        self._defaultBorderRadius: int = 8

    # Properties
    @pyqtProperty(str, notify=backgroundColorChanged)
    def backgroundColor(self) -> str:
        return self._backgroundColor

    @backgroundColor.setter
    def setBackgroundColor(self, value: str):
        if self._backgroundColor != value:
            self._backgroundColor = value
            print(f"backgroundColor changed. New value: {value}")
            self.backgroundColorChanged.emit(value)

    @pyqtProperty(str, notify=secondBackgroundColorChanged)
    def secondBackgroundColor(self) -> str:
        return self._secondBackgroundColor

    @secondBackgroundColor.setter
    def setSecondBackgroundColor(self, value: str):
        if self._secondBackgroundColor != value:
            self._secondBackgroundColor = value
            print(f"secondBackgroundColor changed. New value: {value}")
            self.secondBackgroundColorChanged.emit(value)

    # Остальные свойства и методы аналогично...

    @pyqtProperty(int, notify=defaultMarginChanged)
    def defaultMargin(self) -> int:
        return self._defaultMargin

    @defaultMargin.setter
    def setDefaultMargin(self, value: int):
        if self._defaultMargin != value:
            self._defaultMargin = value
            print(f"margin changed. New value: {value}")
            self.defaultMarginChanged.emit(value)

    # Аналогично для других свойств и методов...
