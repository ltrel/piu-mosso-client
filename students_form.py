from PySide6.QtWidgets import QWidget, QVBoxLayout
from ui.students_ui import Ui_StudentsForm
from teacher_sidebar import TeacherSidebar


class StudentsForm(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.ui = Ui_StudentsForm()
        self.ui.setupUi(self)

        self.ui.sidebar = TeacherSidebar(self)
        self.ui.sidebar_layout.addWidget(self.ui.sidebar)
        self.ui.sidebar.ui.students_button.setStyleSheet('background-color: blue')
