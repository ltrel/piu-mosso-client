from PySide6.QtWidgets import QApplication, QMessageBox


def app_state_ref(widget):
    return widget.window().app_state

def show_message_box(title, text):
    message_box = QMessageBox()
    message_box.setWindowTitle(title)
    message_box.setText(text)
    message_box.exec()
