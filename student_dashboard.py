from PySide6.QtWidgets import QWidget
from ui.student_dashboard_ui import Ui_StudentDashboard
from datetime import datetime
from utils import app_state_ref, time_ms, title_case

class StudentDashboard(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.ui = Ui_StudentDashboard()
        self.ui.setupUi(self)

        self.ui.sign_out_button.clicked.connect(self.sign_out)

    def setup(self):
      app_state = app_state_ref(self)
      # Show next lesson details
      lessons = app_state.api_get('/lessons').json()
      future_lessons = list(filter(lambda x: x['dateTime'] > time_ms(), lessons))
      future_lessons.sort(key=lambda x: x['dateTime'])
      if len(future_lessons) > 0:
        next_lesson = future_lessons[0]

        dt = datetime.fromtimestamp(next_lesson['dateTime'] // 1000)
        dt_string = f'{dt:%A} {dt:%B} {dt.day}, {dt.year} {dt:%I:%M %p}'
        self.ui.date_label.setText(f'Date: {dt_string}')

        self.ui.location_label.setText(f'Location: {next_lesson["location"]}')
        self.ui.lesson_teacher_label.setText(f'Teacher: {next_lesson["teacherName"]}')
        self.ui.instrument_label.setText(f'Instrument: {title_case(next_lesson["instrument"])}')
        self.ui.duration_label.setText(f'Duration: {next_lesson["minutes"]} minutes')
      else:
        self.clear_lesson()

    def sign_out(self):
      parent = self.parent()
      parent.login_form.setup()
      parent.setCurrentWidget(parent.login_form)

    def clear_lesson(self):
      self.ui.date_label.setText('Date:')
      self.ui.location_label.setText('Location:')
      self.ui.lesson_teacher_label.setText('Teacher:')
      self.ui.instrument_label.setText('Instrument')
      self.ui.duration_label.setText('Duration:')
