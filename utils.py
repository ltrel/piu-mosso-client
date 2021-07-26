from PySide6.QtWidgets import QApplication


def app_state_ref():
    widgets = QApplication.topLevelWidgets()
    for widget in widgets:
      if widget.objectName() == 'MainWindow':
        return widget.app_state
    
    raise Exception('MainWindow could not be found')
