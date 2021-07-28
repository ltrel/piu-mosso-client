import requests
import json
from PySide6.QtWidgets import QWidget
from ui.students_ui import Ui_StudentsForm
from teacher_sidebar import TeacherSidebar
from utils import app_state_ref

class StudentsForm(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.ui = Ui_StudentsForm()
        self.ui.setupUi(self)

        self.ui.sidebar = TeacherSidebar(self)
        self.ui.sidebar_layout.addWidget(self.ui.sidebar)
        self.ui.sidebar.ui.students_button.setStyleSheet('background-color: blue')
        self.students = []

    def showEvent(self, event):
        # Get a list of students from the server.
        app_state = app_state_ref(self)
        students_url = app_state.get_api_url('/students')
        res = requests.get(students_url, params={'auth_token': app_state.get_token()})
        self.students = json.loads(res.content)
        # Populate the listview with the students.
        for student in self.students:
            item_string = f'{student["fullName"]} ({student["username"]})'
            self.ui.students_listwidget.addItem(item_string)
        print(res)
