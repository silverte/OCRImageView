import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QAction
#from widgets.canvas_widget import CanvasWidget
#from config import get_config

#from libs.version import __version__

__appname__ = 'image viewer'

#UI파일 연결
form_class = uic.loadUiType("UI/image_viewer_main.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._loadUiInit()
        self._setEvent()

    def _loadUiInit(self):
        '''
        UI init
        :return: None3
        '''
        self.setWindowTitle("{title}".format(title=__appname__))
        #self.setWindowTitle("{title}({version})".format(title=__appname__)),version=__version__))

    def _setEvent(self):
        '''
        Event set
        :return: None
        '''


    def exitAction(self):
        self.close()
        print("Exited")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()
    exit(app.exec_())