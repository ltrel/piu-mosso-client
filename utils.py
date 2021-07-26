from PySide6.QtWidgets import QApplication, QMessageBox


def app_state_ref():
    widgets = QApplication.topLevelWidgets()
    for widget in widgets:
      if widget.objectName() == 'MainWindow':
        return widget.app_state
    
    raise Exception('MainWindow could not be found')

def show_message_box(title, text):
    message_box = QMessageBox()
    message_box.setWindowTitle(title)
    message_box.setText(text)
    message_box.exec()
