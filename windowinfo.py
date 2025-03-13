from PyQt6.QtCore import *

class WindowInfo(QObject):
    widthChanged = pyqtSignal(int)
    heightChanged = pyqtSignal(int)
    titleChanged = pyqtSignal(str)
    nameChanged = pyqtSignal(str)
    iconChanged = pyqtSignal(str)

    def __init__(self, width=0, height=0, title="", name="", icon="", parent=None):
        super().__init__(parent)
        self._width = width
        self._height = height
        self._title = title
        self._name = name
        self._icon = icon

    @pyqtSlot(int)
    def setWidth(self, value):
        self.width = value
    @pyqtSlot(int)
    def setHeight(self, value):
        self.height = value
    @pyqtSlot(str)
    def setTitle(self, value):
        self.title = value



    @pyqtProperty(int)
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if self._width != value:
            self._width = value
            self.widthChanged.emit(value)

    @pyqtProperty(int)
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if self._height != value:
            self._height = value
            self.heightChanged.emit(value)

    @pyqtProperty(str)
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if self._title != value:
            self._title = value
            self.titleChanged.emit(value)

    @pyqtProperty(str)
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if self._name != value:
            self._name = value
            self.nameChanged.emit(value)
    @pyqtProperty(str)
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value):
        if self._icon != value:
            self._icon = value
            self.iconChanged.emit(value)
