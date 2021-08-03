import re
from PySide6.QtWidgets import QMessageBox


def app_state_ref(widget):
    return widget.window().app_state

def show_message_box(title, text):
    message_box = QMessageBox()
    message_box.setWindowTitle(title)
    message_box.setText(text)
    message_box.exec()

def title_case(string):
    pattern = r"[A-Za-z]+('[A-Za-z]+)?"
    replacement = lambda match_obj: match_obj.group(0).capitalize()
    return re.sub(pattern, replacement, string)
