# import sys
# from PyQt5.QtCore import *
# from PyQt5.QtWebEngineWidgets import *
# from PyQt5.QtWidgets import QApplication
#
# app = QApplication(sys.argv)
#
# web = QWebEngineView()
# web.load(QUrl("file:///Users/bjiang1/eclipse-workspace/py_before/Daily-Toolset/file_content_diff/result.html"))
# web.show()
#
# sys.exit(app.exec_())


import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Check the result")
        self.setGeometry(100, 100, 1200, 600)
        self.browser = QWebEngineView()
        self.browser.load(QUrl("file:///Users/bjiang1/eclipse-workspace/py_before/Daily-Toolset/file_content_diff/result.html"))
        # self.browser.load(QUrl(file_path))
        self.setCentralWidget(self.browser)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exit(app.exec_())
