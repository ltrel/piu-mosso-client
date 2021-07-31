import requests
import json
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from ui.students_ui import Ui_StudentsForm
from teacher_sidebar import TeacherSidebar
from utils import app_state_ref

class StudentsForm(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.ui = Ui_StudentsForm()
        self.ui.setupUi(self)

        self.ui.add_button.clicked.connect(self.add_student)
        self.ui.remove_button.clicked.connect(self.remove_student)

        self.ui.sidebar = TeacherSidebar(self)
        self.ui.sidebar_layout.addWidget(self.ui.sidebar)
        self.ui.sidebar.ui.students_button.setStyleSheet('background-color: blue')

        self.all_students = []
        self.teacher_students = []

    def showEvent(self, event):
        app_state = app_state_ref(self)
        # Get a list of all students from the server.
        students_url = app_state.get_api_url('/students')
        res = requests.get(students_url, params={'auth_token': app_state.get_token()})
        self.all_students = json.loads(res.content)
        # Populate the listview with the students.
        for student in self.all_students:
            item_string = f'{student["fullName"]} ({student["username"]})'
            self.ui.students_listwidget.addItem(item_string)

        # Get a list of the teacher's students from the server.
        teacher_students_url = app_state.get_api_url('/teacher-students')
        res = requests.get(teacher_students_url, params={'auth_token': app_state.get_token()})
        self.teacher_students = json.loads(res.content)
        # Populate the listview with the students.
        for student in self.teacher_students:
            item_string = f'{student["fullName"]} ({student["username"]})'
            self.ui.teacher_students_listwidget.addItem(item_string)

    def add_student(self):
        # Get the currently selected student's internal id.
        listwidget_index = self.ui.students_listwidget.currentRow()
        if listwidget_index == -1: return
        student_id = self.all_students[listwidget_index]['studentId']
        
        # Tell the server to add the student to the teacher.
        app_state = app_state_ref(self)
        add_student_url = app_state.get_api_url('/teacher-students')
        res = requests.post(add_student_url, params={'auth_token': app_state.get_token()}, json={
            'studentId': student_id
        })
        # Make sure the request succeeded.
        if res.status_code != 200:
            raise Exception('API Request Failed')


        # Add the student to the teacher's students listwidget if needed.
        item_string = self.ui.students_listwidget.item(listwidget_index).text()
        item_exists = self.ui.teacher_students_listwidget.findItems(item_string, Qt.MatchExactly)
        if not item_exists:
            self.ui.teacher_students_listwidget.addItem(item_string)
        # Add the student's details to the local list of teacher's students
        self.teacher_students.append(self.all_students[listwidget_index])

    def remove_student(self):
        # Get the currently selected student's internal id.
        listwidget_index = self.ui.teacher_students_listwidget.currentRow()
        if listwidget_index == -1: return
        student_id = self.teacher_students[listwidget_index]['studentId']
        
        # Tell the server to remove the student from the teacher.
        app_state = app_state_ref(self)
        add_student_url = app_state.get_api_url('/teacher-students')
        res = requests.delete(add_student_url, params={'auth_token': app_state.get_token()}, json={
            'studentId': student_id
        })
        # Make sure the request succeeded.
        if res.status_code != 200:
            raise Exception('API Request Failed')

        # Remove the student from the teacher's students listwidget.
        self.ui.teacher_students_listwidget.takeItem(listwidget_index)
        # Remove the student from the internal list of teacher's students.
        self.teacher_students.pop(listwidget_index)
