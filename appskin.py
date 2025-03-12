# qml/UnicornUI/appskin.py
from PyQt6.QtCore import *
from PyQt6.QtGui import QColor
from typing import AnyStr, Optional

class Skin(QObject):
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
        
        # Dark+ theme
        self._backgroundColor: str = "#1E1E1E"            # Workspace background
        self._sidebarBackgroundColor: str = "#001F33"    # Sidebar background
        self._foregroundColor: str = "#D4D4D4"          # Main text color
        self._selectionColor: str = "#D7BA7D"           # Text selection color
        self._cursorColor: str = "#AEAFAD"             # Cursor color
        self._insertCursorColor: str = "#FFFFFF"        # Cursor color in insert mode
        self._lineHighlightColor: str = "#0000FF20"     # Line highlight color
        self._activeTabColor: str = "#007ACC"          # Active tab color
        self._inactiveTabColor: str = "#757575"        # Inactive tab color
        self._borderColor: str = "#454545"             # Border color
        self._selectedItemBackgroundColor: str = "#003B71"   # Selected item background color
        self._statusBarBackgroundColor: str = "#001F33"    # Status bar background color
        self._buttonFontColor = self._foregroundColor
        self._buttonBackgroundColor = self._sidebarBackgroundColor
        self._buttonBorderColor :str = "#017ACC2B"# Button border color   # Sidebar background, Main text and selection colors are used for the button's foreground (text), while active tab is a different shade of blue (#AEAFAD). The cursor’s highlighting will be done with this other shading.

        self._defaultMargin: int = 10
        self._defaultBorderSize: int = 2
        self._defaultBorderRadius: int = 8
        print("init skin")

    # Properties
    #@pyqtProperty(QColor, notify=backgroundColorChanged)
    @pyqtProperty(str, notify=backgroundColorChanged)
    def backgroundColor(self) -> str:
        print(f"ask _backgroundColor. return {self._backgroundColor}")
        return self._backgroundColor

    @backgroundColor.setter
    def backgroundColor(self, value: str):
        if self._backgroundColor != value:
            self._backgroundColor = value
            print(f"backgroundColor changed. New value: {value}")
            self.backgroundColorChanged.emit(value)

    @pyqtProperty(str, notify=secondBackgroundColorChanged)
    def secondBackgroundColor(self) -> str:
        return self._sidebarBackgroundColor

    @secondBackgroundColor.setter
    def secondBackgroundColor(self, value: str):
        if self._sidebarBackgroundColor != value:
            self._sidebarBackgroundColor = value
            print(f"secondBackgroundColor changed. New value: {value}")
            self.secondBackgroundColorChanged.emit(value)

    @pyqtProperty(str, notify=mainFontColorChanged)
    def mainFontColor(self) -> str:
        return self._foregroundColor

    @mainFontColor.setter
    def mainFontColor(self, value: str):
        if self._foregroundColor != value:
            self._foregroundColor = value
            print(f"mainFontColor changed. New value: {value}")
            self.mainFontColorChanged.emit(value)

    @pyqtProperty(str, notify=buttonBackgroundColorChanged)
    def buttonBackgroundColor(self) -> str:
        return self._buttonBackgroundColor

    @buttonBackgroundColor.setter
    def buttonBackgroundColor(self, value: str):
        if self._buttonBackgroundColor != value:
            self._buttonBackgroundColor = value
            print(f"buttonBackgroundColor changed. New value: {value}")
            self.buttonBackgroundColorChanged.emit(value)

    @pyqtProperty(str, notify=buttonFontColorChanged)
    def buttonFontColor(self) -> str:
        return self._buttonFontColor

    @buttonFontColor.setter
    def buttonFontColor(self, value: str):
        if self._buttonFontColor != value:
            self._buttonFontColor = value
            print(f"buttonFontColor changed. New value: {value}")
            self.buttonFontColorChanged.emit(value)

    @pyqtProperty(str, notify=buttonBorderColorChanged)
    def buttonBorderColor(self) -> str:
        return self._buttonBorderColor

    @buttonBorderColor.setter
    def buttonBorderColor(self, value: str):
        if self._buttonBorderColor != value:
            self._buttonBorderColor = value
            print(f"buttonBorderColor changed. New value: {value}")
            self.buttonBorderColorChanged.emit(value)

    @pyqtProperty(str, notify=buttonHoveredBackgroundColorChanged)
    def buttonHoveredBackgroundColor(self) -> str:
        return self._buttonHoveredBackgroundColor

    @buttonHoveredBackgroundColor.setter
    def buttonHoveredBackgroundColor(self, value: str):
        if self._buttonHoveredBackgroundColor != value:
            self._buttonHoveredBackgroundColor = value
            print(f"buttonHoveredBackgroundColor changed. New value: {value}")
            self.buttonHoveredBackgroundColorChanged.emit(value)

    @pyqtProperty(str, notify=buttonHoveredFontColorChanged)
    def buttonHoveredFontColor(self) -> str:
        return self._buttonHoveredFontColor

    @buttonHoveredFontColor.setter
    def buttonHoveredFontColor(self, value: str):
        if self._buttonHoveredFontColor != value:
            self._buttonHoveredFontColor = value
            print(f"buttonHoveredFontColor changed. New value: {value}")
            self.buttonHoveredFontColorChanged.emit(value)

    @pyqtProperty(str, notify=buttonHoveredBorderColorChanged)
    def buttonHoveredBorderColor(self) -> str:
        return self._buttonHoveredBorderColor

    @buttonHoveredBorderColor.setter
    def buttonHoveredBorderColor(self, value: str):
        if self._buttonHoveredBorderColor != value:
            self._buttonHoveredBorderColor = value
            print(f"buttonHoveredBorderColor changed. New value: {value}")
            self.buttonHoveredBorderColorChanged.emit(value)

    @pyqtProperty(str, notify=buttonDisabledBackgroundColorChanged)
    def buttonDisabledBackgroundColor(self) -> str:
        return self._buttonDisabledBackgroundColor

    @buttonDisabledBackgroundColor.setter
    def buttonDisabledBackgroundColor(self, value: str):
        if self._buttonDisabledBackgroundColor != value:
            self._buttonDisabledBackgroundColor = value
            print(f"buttonDisabledBackgroundColor changed. New value: {value}")
            self.buttonDisabledBackgroundColorChanged.emit(value)

    @pyqtProperty(str, notify=buttonDisabledFontColorChanged)
    def buttonDisabledFontColor(self) -> str:
        return self._buttonDisabledFontColor

    @buttonDisabledFontColor.setter
    def buttonDisabledFontColor(self, value: str):
        if self._buttonDisabledFontColor != value:
            self._buttonDisabledFontColor = value
            print(f"buttonDisabledFontColor changed. New value: {value}")
            self.buttonDisabledFontColorChanged.emit(value)

    @pyqtProperty(str, notify=buttonDisabledBorderColorChanged)
    def buttonDisabledBorderColor(self) -> str:
        return self._buttonDisabledBorderColor

    @buttonDisabledBorderColor.setter
    def buttonDisabledBorderColor(self, value: str):
        if self._buttonDisabledBorderColor != value:
            self._buttonDisabledBorderColor = value
            print(f"buttonDisabledBorderColor changed. New value: {value}")
            self.buttonDisabledBorderColorChanged.emit(value)

    @pyqtProperty(int, notify=defaultMarginChanged)
    def defaultMargin(self) -> int:
        return self._defaultMargin

    @defaultMargin.setter
    def defaultMargin(self, value: int):
        if self._defaultMargin != value:
            self._defaultMargin = value
            print(f"defaultMargin changed. New value: {value}")
            self.defaultMarginChanged.emit(value)

    @pyqtProperty(int, notify=defaultBorderSizeChanged)
    def defaultBorderSize(self) -> int:
        return self._defaultBorderSize

    @defaultBorderSize.setter
    def defaultBorderSize(self, value: int):
        if self._defaultBorderSize != value:
            self._defaultBorderSize = value
            print(f"defaultBorderSize changed. New value: {value}")
            self.defaultBorderSizeChanged.emit(value)

    @pyqtProperty(int, notify=defaultBorderRadiusChanged)
    def defaultBorderRadius(self) -> int:
        return self._defaultBorderRadius

    @defaultBorderRadius.setter
    def defaultBorderRadius(self, value: int):
        if self._defaultBorderRadius != value:
            self._defaultBorderRadius = value
            print(f"defaultBorderRadius changed. New value: {value}")
            self.defaultBorderRadiusChanged.emit(value)

    @pyqtProperty(str, notify=firstBorderColorChanged)
    def firstBorderColor(self) -> str:
        return self._firstBorderColor

    @firstBorderColor.setter
    def firstBorderColor(self, value: str):
        if self._firstBorderColor != value:
            self._firstBorderColor = value
            print(f"firstBorderColor changed. New value: {value}")
            self.firstBorderColorChanged.emit(value)

    @pyqtProperty(str, notify=secondBorderColorChanged)
    def secondBorderColor(self) -> str:
        return self._secondBorderColor

    @secondBorderColor.setter
    def secondBorderColor(self, value: str):
        if self._secondBorderColor != value:
            self._secondBorderColor = value
            print(f"secondBorderColor changed. New value: {value}")
            self.secondBorderColorChanged.emit(value)

    # Слоты для изменения темы (опционально)
    @pyqtSlot()
    def resetToDefault(self):
        self._backgroundColor: str = "#1E1E1E"            # Workspace background
        self._sidebarBackgroundColor: str = "#001F33"    # Sidebar background
        self._foregroundColor: str = "#D4D4D4"          # Main text color
        self._selectionColor: str = "#D7BA7D"           # Text selection color
        self._cursorColor: str = "#AEAFAD"             # Cursor color
        self._insertCursorColor: str = "#FFFFFF"        # Cursor color in insert mode
        self._lineHighlightColor: str = "#0000FF20"     # Line highlight color
        self._activeTabColor: str = "#007ACC"          # Active tab color
        self._inactiveTabColor: str = "#757575"        # Inactive tab color
        self._borderColor: str = "#454545"             # Border color
        self._selectedItemBackgroundColor: str = "#003B71"   # Selected item background color
        self._statusBarBackgroundColor: str = "#001F33"    # Status bar background color

        self._defaultMargin: int = 10
        self._defaultBorderSize: int = 2
        self._defaultBorderRadius: int = 8



class Skin2(QObject):
    # Сигналы для цветовых свойств
    backgroundColorChanged = pyqtSignal()
    secondBackgroundColorChanged = pyqtSignal()
    mainFontColorChanged = pyqtSignal()
    defaultMarginChanged = pyqtSignal()
    
    # ... остальные сигналы аналогично

    def __init__(self, parent: QObject | None = None):
        super().__init__(parent)
        self.init_default_theme()

    def init_default_theme(self):
        """Инициализация значений темы по умолчанию"""
        # Основные цвета
        self._background_color = QColor("#1E1E1E")
        self._second_background_color = QColor("#001F33")
        self._main_font_color = QColor("#D4D4D4")
        
        # Цвета кнопок
        self._button_background = QColor("#252526")
        self._button_font_color = QColor("#FFFFFF")
        # ... инициализировать все остальные свойства

        # Размеры
        self._default_margin = 10
        self._default_border_size = 2
        self._default_border_radius = 8

    # region Цветовые свойства
    @pyqtProperty(QColor, notify=backgroundColorChanged)
    def backgroundColor(self) -> QColor:
        return self._background_color

    @backgroundColor.setter
    def backgroundColor(self, value: QColor):
        if self._background_color != value:
            self._background_color = value
            self.backgroundColorChanged.emit()

    @pyqtProperty(QColor, notify=secondBackgroundColorChanged)
    def secondBackgroundColor(self) -> QColor:
        return self._second_background_color

    @secondBackgroundColor.setter
    def secondBackgroundColor(self, value: QColor):
        if self._second_background_color != value:
            self._second_background_color = value
            self.secondBackgroundColorChanged.emit()
    # endregion

    # region Свойства размеров
    @pyqtProperty(int, notify=defaultMarginChanged)
    def defaultMargin(self) -> int:
        return self._default_margin

    @defaultMargin.setter
    def defaultMargin(self, value: int):
        if self._default_margin != value:
            self._default_margin = value
            self.defaultMarginChanged.emit()
    # endregion

    @pyqtSlot()
    def resetToDefault(self):
        """Сброс всех настроек к значениям по умолчанию"""
        previous_values = self.__dict__.copy()
        self.init_default_theme()
        
        # Определяем какие свойства изменились
        for prop, value in self.__dict__.items():
            if prop.startswith('_') and previous_values[prop] != value:
                signal_name = f"{prop[1:]}Changed"
                if hasattr(self, signal_name):
                    getattr(self, signal_name).emit()

    # Дополнительные методы
    def to_dict(self) -> dict:
        """Экспорт текущих настроек в словарь"""
        return {
            'background_color': self._background_color.name(),
            'second_background_color': self._second_background_color.name(),
            # ... остальные свойства
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Skin':
        """Импорт настроек из словаря"""
        skin = cls()
        skin.backgroundColor = QColor(data.get('background_color', "#1E1E1E"))
        # ... остальные свойства
        return skin