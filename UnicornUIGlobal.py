# ui/unicornuiglobal.py
from PyQt6.QtCore import *
import os
import sys

class QmlLogWrapper(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        
    def onQmlTrace(self, msg):
        print(f"[QML_TRACE] {msg}")
    
    def onQmlDebug(self, msg):
        print(f"[QML_DEBUG] {msg}")
    
    def onQmlInfo(self, msg):
        print(f"[QML_INFO] {msg}")
    
    def onQmlWarning(self, msg):
        print(f"[QML_WARNING] {msg}")
    
    def onQmlError(self, msg):
        print(f"[QML_ERROR] {msg}")
    
    def onQmlCritical(self, msg):
        print(f"[QML_CRITICAL] {msg}")
    
    def onQmlFatal(self, msg):
        sys.exit(f"[QML_FATAL] {msg}")

class UnicornUIGlobal(QObject):
    _instance = None
    debugGridEnabledChanged = pyqtSignal(bool)
    propertyLoggingEnabledChanged = pyqtSignal(bool)
    fpsBoosterEnabledChanged = pyqtSignal(bool)
    fpsIndicatorEnabledChanged = pyqtSignal(bool)

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, parent=None):
        super().__init__(parent)
        self._debug_grid_enabled = False
        self._property_logging_enabled = False
        self._fps_booster_enabled = False
        self._fps_indicator_enabled = False

    @classmethod
    def self(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    @pyqtProperty(bool, notify=debugGridEnabledChanged)
    def debugGridEnabled(self):
        return self._debug_grid_enabled
    
    
    @pyqtSlot(bool)
    def setDebugGridEnabled(self, value):
        if value != self._debug_grid_enabled:
            self._debug_grid_enabled = value
            if self.propertyLoggingEnabled:
                print(f"debugGridEnabled changed to: {value}")
            self.debugGridEnabledChanged.emit(value)


    @pyqtProperty(bool, notify=propertyLoggingEnabledChanged)
    def propertyLoggingEnabled(self):
        return self._property_logging_enabled
    
    @pyqtSlot(bool)
    def setPropertyLoggingEnabled(self, value):
        if value != self._property_logging_enabled:
            self._property_logging_enabled = value
            if self.propertyLoggingEnabled:
                print(f"propertyLoggingEnabled changed to: {value}")
            self.propertyLoggingEnabledChanged.emit(value)

    @pyqtProperty(bool, notify=fpsBoosterEnabledChanged)
    def fpsBoosterEnabled(self):
        return self._fps_booster_enabled
    
    @pyqtSlot(bool)
    def setFpsBoosterEnabled(self, value):
        if value != self._fps_booster_enabled:
            self._fps_booster_enabled = value
            if self.propertyLoggingEnabled:
                print(f"fpsBoosterEnabled changed to: {value}")
            self.fpsBoosterEnabledChanged.emit(value)

    @pyqtProperty(bool, notify=fpsIndicatorEnabledChanged)
    def fpsIndicatorEnabled(self):
        return self._fps_indicator_enabled
    
    @pyqtSlot(bool)
    def setFpsIndicatorEnabled(self, value):
        if value != self._fps_indicator_enabled:
            self._fps_indicator_enabled = value
            if self.propertyLoggingEnabled:
                print(f"fpsIndicatorEnabled changed to: {value}")
            self.fpsIndicatorEnabledChanged.emit(value)
