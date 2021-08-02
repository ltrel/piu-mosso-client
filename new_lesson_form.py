from PySide6.QtWidgets import QWidget
from ui.new_lesson_ui import Ui_NewLessonForm
from teacher_sidebar import TeacherSidebar

class NewLessonForm(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.ui = Ui_NewLessonForm()
        self.ui.setupUi(self)

        self.ui.sidebar = TeacherSidebar(self)
        self.ui.sidebar_layout.addWidget(self.ui.sidebar)
        self.ui.sidebar.ui.new_button.setStyleSheet('background-color: blue')
