from PySide6.QtWidgets import QWidget
from ui.calendar_ui import Ui_CalendarForm
from teacher_sidebar import TeacherSidebar
from utils import app_state_ref


class CalendarForm(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.ui = Ui_CalendarForm()
        self.ui.setupUi(self)

        self.ui.sidebar = TeacherSidebar(self, 'calendar_button')
        self.ui.sidebar_layout.addWidget(self.ui.sidebar)
        self.lessons = []

    def setup(self):
        app_state = app_state_ref(self)
        pass
