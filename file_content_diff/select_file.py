import sys
import os
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "Select two files to show diff"
        self.file_standard = None
        self.file_compare = None
        self.textbox_first = None
        self.textbox_second = None
        self.button_first = None
        self.button_second = None
        self.button_diff = None
        self.button_clear = None
        self.init_app()

    def init_app(self):
        self.setWindowTitle(self.title)
        self.setGeometry(300, 300, 400, 180)

        self.textbox_first = QLineEdit(self)
        self.textbox_first.move(20, 20)
        self.textbox_first.resize(280, 40)
        self.textbox_second = QLineEdit(self)
        self.textbox_second.move(20, 80)
        self.textbox_second.resize(280, 40)

        self.button_first = QPushButton("select file", self)
        self.button_first.move(300, 30)
        self.button_second = QPushButton("select file", self)
        self.button_second.move(300, 90)
        self.button_diff = QPushButton("show diff", self)
        self.button_diff.move(20, 140)
        self.button_clear = QPushButton("clear", self)
        self.button_clear.move(160, 140)

        self.button_first.clicked.connect(self.on_click_first)
        self.button_second.clicked.connect(self.on_click_second)
        self.button_diff.clicked.connect(self.on_click_diff)
        self.button_clear.clicked.connect(self.on_click_clear)
        self.show()

    @pyqtSlot()
    def on_click_first(self):
        # textboxValue = self.textbox.text()
        # QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok,
        #                      QMessageBox.Ok)
        # self.textbox.setText("")
        file_path = QFileDialog.getOpenFileName(self, 'OpenFile')
        self.textbox_first.setText(file_path[0])
        self.file_standard = file_path[0]

    @pyqtSlot()
    def on_click_second(self):
        file_path = QFileDialog.getOpenFileName(self, 'OpenFile')
        self.textbox_second.setText(file_path[0])
        self.file_compare = file_path[0]

    @pyqtSlot()
    def on_click_diff(self):
        os.system(f"python file_content_diff.py -f1 {self.file_standard} -f2 {self.file_compare}")

    @pyqtSlot()
    def on_click_clear(self):
        self.textbox_first.setText("")
        self.textbox_second.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
