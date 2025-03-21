from PyQt6.QtCore import *
from typing import AnyStr, Optional

class Skin(QObject):
    backgroundColorChanged = pyqtSignal(str)
    foregroundColorChanged = pyqtSignal(str)
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
    selectionColorChanged = pyqtSignal(str)
    cursorColorChanged = pyqtSignal(str)
    insertCursorColorChanged = pyqtSignal(str)
    lineHighlightColorChanged = pyqtSignal(str)
    activeTabColorChanged = pyqtSignal(str)
    inactiveTabColorChanged = pyqtSignal(str)
    borderColorChanged = pyqtSignal(str)
    selectedItemBackgroundColorChanged = pyqtSignal(str)
    statusBarBackgroundColorChanged = pyqtSignal(str)

    # console
    consoleBackgroundColorChanged = pyqtSignal(str)
    consoleBorderColorChanged = pyqtSignal(str)
    consoleTextColorChanged = pyqtSignal(str)
    consoleFontNameChanged = pyqtSignal(str)
    consoleFontSizeChanged = pyqtSignal(int)

    # Dark+ theme
    def __init__(self, parent: QObject | None = None):
        super().__init__(parent)
        
        # Main colors
        self._background_color           = "#1E1E1E"    # Main background
        self._sidebar_background_color   = "#001F33"    # Sidebar background
        self._foreground_color           = "#D4D4D4"    # Main text color
        self._selection_color            = "#D7BA7D"    # Text selection color
        self._cursor_color               = "#AEAFAD"    # Cursor color
        self._insert_cursor_color        = "#FFFFFF"    # Insert mode cursor color
        self._line_highlight_color       = "#0000FF20"  # Line highlight color
        self._active_tab_color           = "#007ACC"    # Active tab color
        self._inactive_tab_color         = "#757575"    # Inactive tab color
        self._border_color               = "#454545"    # Border color
        self._selected_item_background   = "#003B71"    # Selected item background
        self._status_bar_background      = "#001F33"    # Status bar background
        
         # Button colors
        self._button_background          = "#252526"    # Main button background
        self._button_font_color          = "#FFFFFF"    # Button text color
        self._button_border_color        = "#007ACC"    # Button hover border
        self._button_hovered_background  = "#374760"    # Button hover background
        self._button_hovered_font_color  = "#FFFFFF"    # Button hover text color
        self._button_hovered_border      = "#007ACC"    # Button hover border
        self._button_disabled_background = "#313131"    # Disabled button background
        self._button_disabled_font_color = "#8B8B8B"   # Disabled button text color
        self._button_disabled_border     = "#595959"    # Disabled button border
        
         # Sizes
        self._default_margin             = 10           # Default margin value
        self._default_border_size        = 2            # Default border thickness
        self._default_border_radius      = 8            # Default border radius
        
         # Additional colors and properties
        self._first_border_color          = "#007ACC"    # Primary border color
        self._second_border_color         = "#595959"    # Secondary border color

        # console colors and properties
        self._console_background = "#1e1e1e"
        self._console_border_color = "#999998" 
        self._console_text_color  ="#d4d4d4"
        self._console_font_name = "Courier New"
        self._console_font_size = 12

        
        self._defaultMargin: int  = 10
        self._defaultBorderSize: int = 2
        self._defaultBorderRadius: int = 8

    @pyqtProperty(str, notify=foregroundColorChanged) 
    def foregroundColor(self) -> str:
        return self._foreground_color

    @foregroundColor.setter 
    def foregroundColor( self, value: str ):
        if self._foreground_color != value:
            self._foreground_color = value
            print(f"foregroundColor changed. New value: {value}")
            self.foregroundColorChanged.emit(value)

    @pyqtProperty(str, notify=backgroundColorChanged)
    def backgroundColor(self) -> str:
        return self._background_color

    @backgroundColor.setter
    def backgroundColor(self, value: str):
        if self._background_color != value:
            self._background_color = value
            print(f"backgroundColor changed. New value: {value}")
            self.backgroundColorChanged.emit(value)

    @pyqtProperty(str, notify=secondBackgroundColorChanged)
    def secondBackgroundColor(self) -> str:
        return self._sidebar_background_color

    @secondBackgroundColor.setter
    def secondBackgroundColor(self, value: str):
        if self._sidebar_background_color != value:
            self._sidebar_background_color = value
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
        return self._button_background

    @buttonBackgroundColor.setter
    def buttonBackgroundColor(self, value: str):
        if self._button_background != value:
            self._button_background = value
            print(f"_button_background changed. New value: {value}")
            self.buttonBackgroundColorChanged.emit(value)

    @pyqtProperty(str, notify=buttonFontColorChanged)
    def buttonFontColor(self) -> str:
        return self._button_font_color

    @buttonFontColor.setter
    def buttonFontColor(self, value: str):
        if self._button_font_color != value:
            self._button_font_color = value
            print(f"buttonFontColor changed. New value: {value}")
            self.buttonFontColorChanged.emit(value)

    @pyqtProperty(str, notify=buttonBorderColorChanged)
    def buttonBorderColor(self) -> str:
        return self._first_border_color

    @buttonBorderColor.setter
    def buttonBorderColor(self, value: str):
        if self._first_border_color != value:
            self._first_border_color = value
            print(f"buttonBorderColor changed. New value: {value}")
            self.buttonBorderColorChanged.emit(value)

    @pyqtProperty(str, notify=buttonHoveredBackgroundColorChanged)
    def buttonHoveredBackgroundColor(self) -> str:
        return self._button_hovered_background

    @buttonHoveredBackgroundColor.setter
    def buttonHoveredBackgroundColor(self, value: str):
        if self._button_hovered_background != value:
            self._button_hovered_background = value
            print(f"_button_hovered_background changed. New value: {value}")
            self.buttonHoveredBackgroundColorChanged.emit(value)

    @pyqtProperty(str, notify=buttonHoveredFontColorChanged)
    def buttonHoveredFontColor(self) -> str:
        return self._button_hovered_font_color

    @buttonHoveredFontColor.setter
    def buttonHoveredFontColor(self, value: str):
        if self._button_hovered_font_color != value:
            self._button_hovered_font_color = value
            print(f"_button_hovered_font_color changed. New value: {value}")
            self.buttonHoveredFontColorChanged.emit(value)

    @pyqtProperty(str, notify=buttonHoveredBorderColorChanged)
    def buttonHoveredBorderColor(self) -> str:
        return self._button_hovered_border

    @buttonHoveredBorderColor.setter
    def buttonHoveredBorderColor(self, value: str):
        if self._button_hovered_border != value:
            self._button_hovered_border = value
            print(f"buttonHoveredBorderColor changed. New value: {value}")
            self.buttonHoveredBorderColorChanged.emit(value)

    @pyqtProperty(str, notify=buttonDisabledBackgroundColorChanged)
    def buttonDisabledBackgroundColor(self) -> str:
        return self._button_disabled_background

    @buttonDisabledBackgroundColor.setter
    def buttonDisabledBackgroundColor(self, value: str):
        if self._button_disabled_background != value:
            self._button_disabled_background = value
            print(f"buttonDisabledBackgroundColor changed. New value: {value}")
            self.buttonDisabledBackgroundColorChanged.emit(value)

    @pyqtProperty(str, notify=buttonDisabledFontColorChanged)
    def buttonDisabledFontColor(self) -> str:
        return self._button_disabled_font_color

    @buttonDisabledFontColor.setter
    def buttonDisabledFontColor(self, value: str):
        if self._button_disabled_font_color != value:
            self._button_disabled_font_color = value
            print(f"buttonDisabledFontColor changed. New value: {value}")
            self.buttonDisabledFontColorChanged.emit(value)

    @pyqtProperty(str, notify=buttonDisabledBorderColorChanged)
    def buttonDisabledBorderColor(self) -> str:
        return self._button_disabled_border

    @buttonDisabledBorderColor.setter
    def buttonDisabledBorderColor(self, value: str):
        if self._button_disabled_border != value:
            self._button_disabled_border = value
            print(f"buttonDisabledBorderColor changed. New value: {value}")
            self.buttonDisabledBorderColorChanged.emit(value)

    @pyqtProperty(int, notify=defaultMarginChanged)
    def defaultMargin(self) -> int:
        return self._default_margin

    @defaultMargin.setter
    def defaultMargin(self, value: int):
        if self._default_margin != value:
            self._default_margin = value
            print(f"defaultMargin changed. New value: {value}")
            self.defaultMarginChanged.emit(value)

    @pyqtProperty(int, notify=defaultBorderSizeChanged)
    def defaultBorderSize(self) -> int:
        return self._default_border_size

    @defaultBorderSize.setter
    def defaultBorderSize(self, value: int):
        if self._default_border_size != value:
            self._default_border_size = value
            print(f"defaultBorderSize changed. New value: {value}")
            self.defaultBorderSizeChanged.emit(value)

    @pyqtProperty(int, notify=defaultBorderRadiusChanged)
    def defaultBorderRadius(self) -> int:
        return self._default_border_radius

    @defaultBorderRadius.setter
    def defaultBorderRadius(self, value: int):
        if self._default_border_radius != value:
            self._default_border_radius = value
            print(f"defaultBorderRadius changed. New value: {value}")
            self.defaultBorderRadiusChanged.emit(value)

    @pyqtProperty(str, notify=firstBorderColorChanged)
    def firstBorderColor(self) -> str:
        return self._button_border_color

    @firstBorderColor.setter
    def firstBorderColor(self, value: str):
        if self._button_border_color != value:
            self._button_border_color = value
            print(f"firstBorderColor changed. New value: {value}")
            self.firstBorderColorChanged.emit(value)

    @pyqtProperty(str, notify=secondBorderColorChanged)
    def secondBorderColor(self) -> str:
        return self._second_border_color

    @secondBorderColor.setter
    def secondBorderColor(self, value: str):
        if self._second_border_color != value:
            self._second_border_color = value
            print(f"secondBorderColor changed. New value: {value}")
            self.secondBorderColorChanged.emit(value)

    @pyqtProperty(str, notify=selectionColorChanged) 
    def selectionColor( self ) -> str:
        return self._selection_color

    @selectionColor.setter 
    def selectionColor( self, value: str ):
        if self._selection_color != value:
            self._selection_color = value
            print(f"selectionColor changed. New value: {value}")
            self.selectionColorChanged.emit(value)

    @pyqtProperty(str, notify=cursorColorChanged) 
    def cursorColor( self ) -> str:
        return self._cursor_color

    @cursorColor.setter 
    def cursorColor( self, value: str ):
        if self._cursor_color != value:
            self._cursor_color = value
            print(f"cursorColor changed. New value: {value}")
            self.cursorColorChanged.emit(value)

    @pyqtProperty(str, notify=insertCursorColorChanged) 
    def insertCursorColor( self ) -> str:
        return self._insert_cursor_color

    @insertCursorColor.setter 
    def insertCursorColor( self, value: str ):
        if self._insert_cursor_color != value:
            self._insert_cursor_color = value
            print(f"insertCursorColor changed. New value: {value}")
            self.insertCursorColorChanged.emit(value)

    @pyqtProperty(str, notify=lineHighlightColorChanged) 
    def lineHighlightColor( self ) -> str:
        return self._line_highlight_color

    @lineHighlightColor.setter 
    def lineHighlightColor( self, value: str ):
        if self._line_highlight_color != value:
            self._line_highlight_color = value
            print(f"lineHighlightColor changed. New value: {value}")
            self.lineHighlightColorChanged.emit(value)

    @pyqtProperty(str, notify=activeTabColorChanged) 
    def activeTabColor( self ) -> str:
        return self._active_tab_color

    @activeTabColor.setter 
    def activeTabColor( self, value: str ):
        if self._active_tab_color != value:
            self._active_tab_color = value
            print(f"activeTabColor changed. New value: {value}")
            self.activeTabColorChanged.emit(value)

    @pyqtProperty(str, notify=inactiveTabColorChanged) 
    def inactiveTabColor( self ) -> str:
        return self._inactive_tab_color

    @inactiveTabColor.setter 
    def inactiveTabColor( self, value: str ):
        if self._inactive_tab_color != value:
            self._inactive_tab_color = value
            print(f"inactiveTabColor changed. New value: {value}")
            self.inactiveTabColorChanged.emit(value)

    @pyqtProperty(str, notify=borderColorChanged) 
    def borderColor( self ) -> str:
        return self._border_color

    @borderColor.setter 
    def borderColor( self, value: str ):
        if self._border_color != value:
            self._border_color = value
            print(f"borderColor changed. New value: {value}")
            self.borderColorChanged.emit(value)

    @pyqtProperty(str, notify=selectedItemBackgroundColorChanged) 
    def selectedItemBackground( self ) -> str:
        return self._selected_item_background

    @selectedItemBackground.setter 
    def selectedItemBackground( self, value: str ):
        if self._selected_item_background != value:
            self._selected_item_background = value
            print(f"selectedItemBackground changed. New value: {value}")
            self.selectedItemBackgroundColorChanged.emit(value)

    @pyqtProperty(str, notify=statusBarBackgroundColorChanged) 
    def statusBarBackground( self ) -> str:
        return self._status_bar_background

    @statusBarBackground.setter 
    def statusBarBackground( self, value: str ):
        if self._status_bar_background != value:
            self._status_bar_background = value
            print(f"statusBarBackground changed. New value: {value}")
            self.statusBarBackgroundColorChanged.emit(value)



    # For _console_background
    @pyqtProperty(str, notify=consoleBackgroundColorChanged)
    def consoleBackground(self) -> str:
        return self._console_background

    @consoleBackground.setter
    def consoleBackground(self, value: str):
        if self._console_background != value:
            self._console_background = value
            print(f"consoleBackground changed. New value: {value}")
            self.consoleBackgroundColorChanged.emit(value)

    # For _console_border_color
    @pyqtProperty(str, notify=consoleBorderColorChanged)
    def consoleBorder(self) -> str:
        return self._console_border_color

    @consoleBorder.setter
    def consoleBorder(self, value: str):
        if self._console_border_color != value:
            self._console_border_color = value
            print(f"consoleBorder changed. New value: {value}")
            self.consoleBorderColorChanged.emit(value)

    # For _console_text_color
    @pyqtProperty(str, notify=consoleTextColorChanged)
    def consoleTextColor(self) -> str:
        return self._console_text_color

    @consoleTextColor.setter
    def consoleTextColor(self, value: str):
        if self._console_text_color != value:
            self._console_text_color = value
            print(f"consoleText changed. New value: {value}")
            self.consoleTextColorChanged.emit(value)

    # For _console_font_name
    @pyqtProperty(str, notify=consoleFontNameChanged)
    def consoleFontName(self) -> str:
        return self._console_font_name

    @consoleFontName.setter
    def consoleFontName(self, value: str):
        if self._console_font_name != value:
            self._console_font_name = value
            print(f"consoleFontName changed. New value: {value}")
            self.consoleFontNameChanged.emit(value)

    # For _console_font_size
    @pyqtProperty(int, notify=consoleFontSizeChanged)
    def consoleFontSize(self) -> int:
        return self._console_font_size

    @consoleFontSize.setter
    def consoleFontSize(self, value: int):
        if self._console_font_size != value:
            self._console_font_size = value
            print(f"consoleFontSize changed. New value: {value}")
            self.consoleFontSizeChanged.emit(value)