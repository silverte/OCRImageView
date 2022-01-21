import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.Qt import QFileSystemModel
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot
import cv2

__appname__ = 'image viewer'

#UI파일 연결
form_class = uic.loadUiType("UI/image_viewer_main.ui")[0]

# 화면을 띄우는데 사용되는 Class 선언
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

        self.path_root = QtCore.QDir.cleanPath('/Users/silverte')
        self.model = QFileSystemModel()
        self.model.setRootPath(self.path_root)

        self.index_root = self.model.index(self.model.rootPath())

        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.index_root)
        self.treeView.clicked.connect(self.on_treeView_clicked)

    @pyqtSlot(QtCore.QModelIndex)
    def on_treeView_clicked(self, index):
        index_item = self.model.index(index.row(), 0, index.parent())

        file_name = self.model.fileName(index_item)
        file_path = self.model.filePath(index_item)

        print(file_name, file_path)

        pixmap = QtGui.QPixmap(file_path)
        w = self.label_img.width()
        h = self.label_img.height()
        self.label_img.setPixmap(pixmap.scaled(w, h, QtCore.Qt.KeepAspectRatio))
        self.show()

    def _setEvent(self):
        '''
        Event set
        :return: None
        '''
        self.action_exit.triggered.connect(self.exitAction)
        self.action_save.triggered.connect(self.saveAction)
        self.checkBox_gray.stateChanged.connect(self.grayScaleAction)

    def grayScaleAction(self):
        print(self)
        #self.gray = cv2.cvtColor()


    def exitAction(self):
        self.close()
        print("Exited")

    def saveAction(self):
        file_name = QFileDialog.getSaveFileName(self, 'save image', '/Users/silverte')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()
    exit(app.exec_())