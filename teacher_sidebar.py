from PySide6.QtWidgets import QWidget
from ui.teacher_sidebar_ui import Ui_TeacherSidebar
from utils import app_state_ref


class TeacherSidebar(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.ui = Ui_TeacherSidebar()
        self.ui.setupUi(self)

    def showEvent(self, event):
        name = app_state_ref(self).fullname
        self.ui.user_label.setText(f'You are signed in as:\n{name}')
