import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from ui.mainwindow_ui import Ui_MainWindow
from register_form import RegisterForm

if __name__ == '__main__':
  app = QApplication(sys.argv)

  window = QMainWindow()
  main_ui = Ui_MainWindow()
  main_ui.setupUi(window)

  register_form = RegisterForm(None)
  window.setCentralWidget(register_form)

  window.show()

  sys.exit(app.exec())
