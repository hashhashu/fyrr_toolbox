import sys
import window 
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow

print("Hi, I'm your personal assistant ^^")
app = QApplication(sys.argv)
mainWindow = QMainWindow()
ui = window.Ui_MainWindow()
ui.setupUi(mainWindow)
mainWindow.show()
sys.exit(app.exec())