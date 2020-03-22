from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
import os
import os.path

class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        uic.loadUi('main.ui', self)
        self.InitUI()
        self.Handle_Buttons()
    
    def InitUI(self):
        ##contain all ui changes in loading
        pass
    
    def Handle_Buttons(self):
        ##handle all buttons in the app
        self.pushButton.clicked.connect(self.Download)

    def handle_Progress(self):
        ##calculate the progress
        pass

    def handle_Browse(self):
        ##enable bwosing ro our os, browse, save location
        pass

    def Download(self):
        ##downloading any files
        print("Starting Download...")
    
    def Save_Browse(self):
        ##save location
        pass

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__=='__main__':
    main()