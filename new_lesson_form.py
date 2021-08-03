import json
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QDate, QTime, QDateTime
from ui.new_lesson_ui import Ui_NewLessonForm
from teacher_sidebar import TeacherSidebar
from utils import app_state_ref, title_case


class NewLessonForm(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.ui = Ui_NewLessonForm()
        self.ui.setupUi(self)

        self.ui.cancel_button.clicked.connect(self.clear_fields)

        self.ui.sidebar = TeacherSidebar(self)
        self.ui.sidebar_layout.addWidget(self.ui.sidebar)
        self.ui.sidebar.ui.new_button.setStyleSheet('background-color: blue')

        self.students = []

    def setup(self):
        # Clear what was already in the combo boxes
        self.ui.student_combo.clear()
        self.ui.instrument_combo.clear()
        self.ui.location_combo.clear()

        app_state = app_state_ref(self)
        # Get students
        res = app_state.api_get('/teacher-students')
        self.students = json.loads(res.content)
        for student in self.students:
            item_string = f'{student["fullName"]} ({student["username"]})'
            self.ui.student_combo.addItem(item_string)

        # Get instruments
        res = app_state.api_get('/instruments')
        instruments = map(lambda x: title_case(x['instrumentName']),
                          json.loads(res.content))
        self.ui.instrument_combo.addItems(instruments)

        # Get locations
        res = app_state.api_get('/locations')
        instruments = map(lambda x: title_case(x['instrumentName']),
                          json.loads(res.content))
        self.ui.location_combo.addItems(instruments)
        self.clear_fields()

    def clear_fields(self):
        self.ui.student_combo.setCurrentIndex(-1)
        self.ui.location_combo.setCurrentIndex(-1)
        self.ui.instrument_combo.setCurrentIndex(-1)

        # 12 PM Today
        self.ui.time_edit.setTime(QTime(12, 0))
        today = QDateTime.currentDateTime().date()
        self.ui.date_calendar.setSelectedDate(today)
