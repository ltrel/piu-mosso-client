from PySide6.QtWidgets import QWidget
from ui.last_lesson_ui import Ui_LastLessonForm
from teacher_sidebar import TeacherSidebar
from utils import app_state_ref


class LastLessonForm(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.ui = Ui_LastLessonForm()
        self.ui.setupUi(self)

        self.ui.sidebar = TeacherSidebar(self)
        self.ui.sidebar_layout.addWidget(self.ui.sidebar)
        self.ui.sidebar.ui.last_button.setStyleSheet('background-color: blue')
    
    def setup(self):
      pass
