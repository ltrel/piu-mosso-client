from PySide6.QtWidgets import QWidget
from ui.teacher_sidebar_ui import Ui_TeacherSidebar
from utils import app_state_ref


class TeacherSidebar(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.ui = Ui_TeacherSidebar()
        self.ui.setupUi(self)

        self.ui.sign_out_button.clicked.connect(self.sign_out)

    def sign_out(self):
        stacked_widget = self.window().ui.stacked_widget
        stacked_widget.setCurrentWidget(stacked_widget.login_form)

    def showEvent(self, event):
        name = app_state_ref(self).fullname
        self.ui.user_label.setText(f'You are signed in as:\n{name}')
