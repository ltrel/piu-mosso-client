import os
from PySide6.QtWidgets import QWidget, QFileDialog
from ui.student_dashboard_ui import Ui_StudentDashboard
from datetime import datetime
from utils import app_state_ref, time_ms, title_case, show_message_box


class StudentDashboard(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.ui = Ui_StudentDashboard()
        self.ui.setupUi(self)

        self.ui.sign_out_button.clicked.connect(self.sign_out)
        self.ui.teacher_combo.currentIndexChanged.connect(self.list_files)
        self.ui.download_button.clicked.connect(self.download_file)

    def setup(self):
        app_state = app_state_ref(self)
        # Show next lesson details
        lessons = app_state.api_get('/lessons').json()
        future_lessons = list(
            filter(lambda x: x['dateTime'] > time_ms(), lessons))
        future_lessons.sort(key=lambda x: x['dateTime'])
        if len(future_lessons) > 0:
            next_lesson = future_lessons[0]

            # Format the date
            dt = datetime.fromtimestamp(next_lesson['dateTime'] // 1000)
            dt_string = f'{dt:%A} {dt:%B} {dt.day}, {dt.year} {dt:%I:%M %p}'
            self.ui.date_label.setText(f'Date: {dt_string}')

            self.ui.location_label.setText(
                f'Location: {next_lesson["location"]}')
            self.ui.lesson_teacher_label.setText(
                f'Teacher: {next_lesson["teacherName"]}')
            self.ui.instrument_label.setText(
                f'Instrument: {title_case(next_lesson["instrument"])}')
            self.ui.duration_label.setText(
                f'Duration: {next_lesson["minutes"]} minutes')
        else:
            self.clear_lesson()

        # Populate combo box with list of the student's teachers
        self.teachers = app_state.api_get('/teacher-students').json()
        self.ui.teacher_combo.clear()
        for teacher in self.teachers:
            item_string = f'{teacher["fullName"]}'
            self.ui.teacher_combo.addItem(item_string)

        # Show student's name above sign out button
        name = app_state.fullname
        self.ui.user_label.setText(f'You are signed in as:\n{name}')

    def clear_lesson(self):
        # Clear all the textboxes that show the details of the next lesson
        self.ui.date_label.setText('Date:')
        self.ui.location_label.setText('Location:')
        self.ui.lesson_teacher_label.setText('Teacher:')
        self.ui.instrument_label.setText('Instrument')
        self.ui.duration_label.setText('Duration:')

    def list_files(self):
        self.ui.files_listwidget.clear()
        # Get the id of the selected teacher
        selected_index = self.ui.teacher_combo.currentIndex()
        if selected_index == -1:
            self.ui.files_teacher_label.setText(
                'Showing files shared with you by:')
            return
        teacher_id = self.teachers[selected_index]['teacherId']

        # Show name of student in label
        teacher_name = self.teachers[selected_index]['fullName']
        self.ui.files_teacher_label.setText(
            f'Showing files shared with you by: {teacher_name}')

        app_state = app_state_ref(self)
        files = app_state.api_get('/files').json()
        self.shown_files = list(
            filter(lambda x: x['teacherId'] == teacher_id, files))
        for file in self.shown_files:
            self.ui.files_listwidget.addItem(file['fileName'])

    def sign_out(self):
        # Reset the login form and go back to it
        parent = self.parent()
        parent.login_form.setup()
        parent.setCurrentWidget(parent.login_form)

    def download_file(self):
        # Get the id of the currently selected file
        selected_index = self.ui.files_listwidget.currentRow()
        if selected_index == -1:
            show_message_box('User input error', 'No file selected')
            return
        file_id = self.shown_files[selected_index]['id']

        # Download the file from the server
        app_state = app_state_ref(self)
        res = app_state.api_get('/files/download', {'fileId': file_id})

        # Write the file to disk at the location specified by the user
        default_name = self.shown_files[selected_index]['fileName']
        default_path = os.path.expanduser(f'~/Documents/{default_name}')
        file_path = QFileDialog.getSaveFileName(self, dir=default_path)[0]
        if file_path == '':
            return
        with open(file_path, 'wb') as output_file:
            output_file.write(res.content)
