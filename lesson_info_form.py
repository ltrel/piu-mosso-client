from datetime import datetime
from PySide6.QtWidgets import QWidget
from ui.lesson_info_ui import Ui_LessonInfoForm
from utils import app_state_ref, title_case


class LessonInfoForm(QWidget):
    def __init__(self, parent, lesson_json=None):
        super().__init__(parent)

        self.ui = Ui_LessonInfoForm()
        self.ui.setupUi(self)

        # If there is no lesson to show, do nothing
        if(lesson_json == None):
            return

        self.ui.discard_button.clicked.connect(self.discard_notes)
        self.ui.save_button.clicked.connect(self.save_notes)

        self.lesson_id = lesson_json['id']
        self.original_notes = lesson_json['notes']
        self.original_attendance = bool(lesson_json['attendance'])

        # Put lesson notes in text box
        self.ui.notes_textbox.setPlainText(lesson_json['notes'])

        # Fill in the lesson details
        self.ui.student_label.setText(f'Student: {lesson_json["studentName"]}')
        self.ui.duration_label.setText(
            f'Duration: {lesson_json["minutes"]} minutes')
        self.ui.location_label.setText(f'Location: {lesson_json["location"]}')
        self.ui.instrument_label.setText(
            f'Instrument: {title_case(lesson_json["instrument"])}')
        self.ui.attendance_checkbox.setChecked(bool(lesson_json['attendance']))

        dt = datetime.fromtimestamp(lesson_json['dateTime'] // 1000)
        dt_string = f'{dt:%A} {dt:%B} {dt.day}, {dt.year} {dt:%I:%M %p}'
        self.ui.date_label.setText(f'Date: {dt_string}')

    def discard_notes(self):
        self.ui.notes_textbox.setPlainText(self.original_notes)
        self.ui.attendance_checkbox.setChecked(self.original_attendance)
        # If this widget is on top of the calendar screen,
        # return to the calendar
        grandparent = self.parent().parent()
        calendar_form = self.window().ui.stacked_widget.calendar_form
        if grandparent == calendar_form:
            grandparent.ui.stacked_widget.setCurrentWidget(grandparent.ui.calendar_page)

    def save_notes(self):
        app_state = app_state_ref(self)
        app_state.api_post('/lessons/notes', {
            'lessonId': self.lesson_id,
            'text': self.ui.notes_textbox.toPlainText(),
            'attendance': self.ui.attendance_checkbox.isChecked()
        })
        # If this widget is on top of the calendar screen, refresh the
        # calendar's lesson details and return to the calendar
        grandparent = self.parent().parent()
        calendar_form = self.window().ui.stacked_widget.calendar_form
        if grandparent == calendar_form:
            grandparent.refresh_lessons()
            grandparent.ui.stacked_widget.setCurrentWidget(grandparent.ui.calendar_page)
