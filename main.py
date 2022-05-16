import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QLineEdit, QMessageBox
from PyQt5.QtWidgets import QLabel, QGridLayout, QWidget, QDesktopWidget, QTextEdit, QPushButton, QFileDialog


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

        def newFile():
            self.textbox.setPlainText("")

        def openFile():
            filename = QFileDialog.getOpenFileName(self,'Open File')
            if filename[0]:
                f = open(filename[0],'r')
                with f:
                    data = f.read()
                    self.textbox.setText(data)

        def saveFile():
            txt = self.textbox.toPlainText()
            dlg = QFileDialog()
            dlg.setFileMode(QFileDialog.AnyFile)
            filenames = []
            if(dlg.exec_()):
                filenames = dlg.selectedFiles()
                f = open(filenames[0], 'w')
                f.write(txt)
                f.close()

        #Toolbar
        buttonNewFile = QPushButton('', self)
        buttonNewFile.setStyleSheet("background-image : url(img/newfile.png);")
        buttonNewFile.setToolTip('Create empty file')
        buttonNewFile.resize(35, 35)
        buttonNewFile.move(50,30)
        buttonNewFile.clicked.connect(newFile)

        buttonOpenFile = QPushButton('', self)
        buttonOpenFile.setStyleSheet("background-image : url(img/openfile.png);")
        buttonOpenFile.setToolTip('Open existing file')
        buttonOpenFile.resize(35, 35)
        buttonOpenFile.move(85,30)
        buttonOpenFile.clicked.connect(openFile)

        buttonOpenFile = QPushButton('', self)
        buttonOpenFile.setStyleSheet("background-image : url(img/savefile.png);")
        buttonOpenFile.setToolTip('Save current file')
        buttonOpenFile.resize(35, 35)
        buttonOpenFile.move(120,30)
        buttonOpenFile.clicked.connect(saveFile)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
