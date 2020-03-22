from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
import os
import os.path

class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        uic.loadUi('main.ui', self)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__=='__main__':
    main()