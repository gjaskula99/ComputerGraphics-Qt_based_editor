import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QLineEdit, QMessageBox
from PyQt5.QtWidgets import QLabel, QGridLayout, QWidget, QDesktopWidget, QTextEdit, QPushButton

import editorIO

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Editor'
        self.initUI()
    
    def initUI(self):
        self.resize(800, 600)
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        self.setWindowTitle(self.title)
    
        #Editbox
        self.textbox = QTextEdit(self)
        self.textbox.move(50, 80)
        self.textbox.resize(700, 500)
        self.textbox.setAlignment(Qt.AlignLeft)

        #Toolbar
        button = QPushButton('', self)
        button.setStyleSheet("background-image : url(img/newfile.png);")
        button.setToolTip('Create empty file')
        button.resize(35, 35)
        button.move(50,30)
        button.clicked.connect(editorIO.newFile)

        self.show()
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())