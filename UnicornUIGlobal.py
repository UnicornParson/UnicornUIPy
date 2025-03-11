
from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot, Qt, pyqtProperty
import sys

class QmlLogWrapper(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
    
    @pyqtSlot(str)
    def onQmlTrace(self, msg):
        print(f"[QML_TRACE] {msg}")
        
    @pyqtSlot(str) 
    def onQmlDebug(self, msg):
        print(f"[QML_DEBUG] {msg}") 
        
    @pyqtSlot(str)
    def onQmlInfo(self, msg): 
        print(f"[QML_INFO] {msg}")
        
    @pyqtSlot(str)
    def onQmlWarning(self, msg):
        print(f"[QML_WARNING] {msg}", file=sys.stderr)
        
    @pyqtSlot(str)
    def onQmlError(self, msg):
        print(f"[QML_ERROR] {msg}", file=sys.stderr)
        
    @pyqtSlot(str)
    def onQmlCritical(self, msg):
        print(f"[QML_CRITICAL] {msg}", file=sys.stderr)
        
    @pyqtSlot(str)
    def onQmlFatal(self, msg):
        sys.exit(f"[QML_FATAL] {msg}")