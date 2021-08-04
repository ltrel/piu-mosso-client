import json
from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import QDate, QTime, QDateTime
from ui.new_lesson_ui import Ui_NewLessonForm
from teacher_sidebar import TeacherSidebar
from utils import app_state_ref, title_case, show_message_box


class NewLessonForm(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.ui = Ui_NewLessonForm()
        self.ui.setupUi(self)

        self.ui.cancel_button.clicked.connect(self.clear_fields)
        self.ui.create_button.clicked.connect(self.create_lesson)

        self.ui.sidebar = TeacherSidebar(self)
        self.ui.sidebar_layout.addWidget(self.ui.sidebar)
        self.ui.sidebar.ui.new_button.setStyleSheet('background-color: blue')

        self.students = []
        self.instruments = []
        self.locations = []

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

        # Get locations
        res = app_state.api_get('/locations')
        self.locations = json.loads(res.content)
        location_names = map(lambda x: x['locationName'],
                             self.locations)
        self.ui.location_combo.addItems(location_names)

        # Get instruments
        res = app_state.api_get('/instruments')
        self.instruments = json.loads(res.content)
        instrument_names = map(lambda x: title_case(x['instrumentName']),
                               self.instruments)
        self.ui.instrument_combo.addItems(instrument_names)
        self.clear_fields()

    def create_lesson(self):
        # Get application state reference.
        app_state = app_state_ref(self)

        # Get text from instrument and location combo boxes as lowercase.
        instrument_text = self.ui.instrument_combo.currentText().lower()
        location_text = self.ui.location_combo.currentText()

        # Make sure all fields have been filled.
        if self.ui.student_combo.currentIndex() == -1:
            show_message_box('User input error', 'No student selected.')
            return
        elif location_text == '':
            show_message_box('User input error', 'No location specified.')
            return
        elif instrument_text == '':
            show_message_box('User input error', 'No instrument specified.')
            return

        # Offer to add the instrument to the database if it doesn't exist.
        location_names = map(lambda x: x['locationName'], self.locations)
        if location_text not in location_names:
            msg_text = f'The location "{location_text}" does not exist in the '\
                'database, would you like to proceed by adding it?'
            msg_title = 'Location not found'
            result = QMessageBox.question(
                self, msg_title, msg_text, QMessageBox.Yes, QMessageBox.No)
            if result != QMessageBox.Yes:
                return
            # Add the location to the database and combo box.
            app_state.api_post('/locations', {'locationName': location_text})
            self.ui.location_combo.addItem(location_text)

        # Offer to add the location to the database if it doesn't exist.
        instrument_names = map(lambda x: x['instrumentName'], self.instruments)
        if instrument_text not in instrument_names:
            msg_text = f'The instrument "{title_case(instrument_text)}" does '\
                'not exist in the database, would you like to proceed by '\
                'adding it?'
            msg_title = 'Instrument not found'
            result = QMessageBox.question(
                self, msg_title, msg_text, QMessageBox.Yes, QMessageBox.No)
            if result != QMessageBox.Yes:
                return
            # Add the instrument to the database and combo box.
            app_state.api_post(
                '/instruments', {'instrumentName': instrument_text})
            self.ui.instrument_combo.addItem(title_case(instrument_text))

        # Format the date.
        date = self.ui.date_calendar.selectedDate()
        time = self.ui.time_edit.time()
        unix_ms = QDateTime(date, time).toMSecsSinceEpoch()

        # Get the id of the selected student.
        selected_student = self.students[self.ui.student_combo.currentIndex()]
        student_id = selected_student['studentId']

        # Create the lesson.
        app_state.api_post('/lessons', {
            'studentId': student_id,
            'instrument': instrument_text,
            'location': location_text,
            'dateTime': unix_ms,
            # TODO: allow the user to choose the number of minutes.
            'minutes': 30,
        })

        show_message_box('Success', 'Lesson created successfully.')
        self.clear_fields()

    def clear_fields(self):
        self.ui.student_combo.setCurrentIndex(-1)
        self.ui.location_combo.setCurrentIndex(-1)
        self.ui.instrument_combo.setCurrentIndex(-1)

        # 12 PM Today
        self.ui.time_edit.setTime(QTime(12, 0))
        today = QDateTime.currentDateTime().date()
        self.ui.date_calendar.setSelectedDate(today)
