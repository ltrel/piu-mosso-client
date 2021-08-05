from datetime import datetime
from PySide6.QtWidgets import QWidget
from ui.lesson_info_ui import Ui_LessonInfoForm
from utils import app_state_ref, title_case


class LessonInfoForm(QWidget):
    def __init__(self, parent, lesson_json=None):
        super().__init__(parent)

        self.ui = Ui_LessonInfoForm()
        self.ui.setupUi(self)

        # Fill in the lesson details
        self.ui.student_label.setText(f'Student: {lesson_json["studentName"]}')
        self.ui.duration_label.setText(
            f'Duration: {lesson_json["minutes"]} minutes')
        self.ui.location_label.setText(f'Location: {lesson_json["location"]}')
        self.ui.instrument_label.setText(
            f'Instrument: {title_case(lesson_json["instrument"])}')

        dt = datetime.fromtimestamp(lesson_json['dateTime'] // 1000)
        dt_string = f'{dt:%A} {dt:%B} {dt.day}, {dt.year} {dt:%I:%M %p}'
        self.ui.date_label.setText(f'Date: {dt_string}')
