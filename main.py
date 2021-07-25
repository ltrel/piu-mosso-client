import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from ui.mainwindow_ui import Ui_MainWindow
from register_form import RegisterForm
from mainwindow import MainWindow

if __name__ == '__main__':
  app = QApplication(sys.argv)

  main_window = MainWindow()
  main_window.show()

  sys.exit(app.exec())
