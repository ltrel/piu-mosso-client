import json
import os
from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Qt
from ui.files_ui import Ui_FilesForm
from teacher_sidebar import TeacherSidebar
from utils import app_state_ref, show_message_box


class FilesForm(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.ui = Ui_FilesForm()
        self.ui.setupUi(self)

        self.ui.sidebar = TeacherSidebar(self, 'files_button')
        self.ui.sidebar_layout.addWidget(self.ui.sidebar)

        self.ui.upload_button.clicked.connect(self.upload_file)
        self.ui.student_combo.currentIndexChanged.connect(self.list_files)

        self.students = []
        self.shown_files = []

    def setup(self):
        # Get list of teacher's students from the server
        app_state = app_state_ref(self)
        self.students = json.loads(
            app_state.api_get('/teacher-students').content)
        self.ui.student_combo.clear()
        for student in self.students:
            item_string = f'{student["fullName"]} ({student["username"]})'
            self.ui.student_combo.addItem(item_string)

        # Clear student combo box selection
        self.ui.student_combo.setCurrentIndex(-1)

    def upload_file(self):
        # Get the id of the selected student
        selected_index = self.ui.student_combo.currentIndex()
        if selected_index == -1:
            show_message_box('User input error', 'No student selected')
            return
        student_id = self.students[selected_index]['studentId']

        # Prompt the user to select a file
        documents_dir = os.path.expanduser('~/Documents')
        file_path = QFileDialog.getOpenFileName(self, dir=documents_dir)[0]
        if file_path == '':
            return

        # Send the file to the server
        app_state = app_state_ref(self)
        app_state.api_post(
            '/files', files={'file': open(file_path, 'rb')}, data={'studentId': student_id})

        # Refresh the list of files
        self.list_files()

    def list_files(self):
        self.ui.files_listwidget.clear()
        # Get the id of the selected student
        selected_index = self.ui.student_combo.currentIndex()
        if selected_index == -1:
            return
        student_id = self.students[selected_index]['studentId']

        app_state = app_state_ref(self)
        files = json.loads(app_state.api_get('/files').content)
        self.shown_files = list(
            filter(lambda x: x['studentId'] == student_id, files))
        for file in self.shown_files:
            self.ui.files_listwidget.addItem(file['fileName'])
