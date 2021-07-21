import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from ui.mainwindow_ui import Ui_MainWindow

if __name__ == '__main__':
  app = QApplication(sys.argv)

  window = QMainWindow()
  Ui_MainWindow().setupUi(window)
  window.show()

  sys.exit(app.exec())
