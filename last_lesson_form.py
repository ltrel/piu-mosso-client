import json
from PySide6.QtWidgets import QWidget
from ui.last_lesson_ui import Ui_LastLessonForm
from lesson_info_form import LessonInfoForm
from teacher_sidebar import TeacherSidebar
from utils import app_state_ref, time_ms


class LastLessonForm(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.ui = Ui_LastLessonForm()
        self.ui.setupUi(self)

        self.ui.sidebar = TeacherSidebar(self)
        self.ui.sidebar_layout.addWidget(self.ui.sidebar)
        self.ui.sidebar.ui.last_button.setStyleSheet('background-color: blue')

        self.ui.lesson_info = None
    
    def setup(self):
        # If there is already a LessonInfoForm here, get rid of it
        if self.ui.lesson_info != None:
            self.ui.lesson_info_layout.removeWidget(self.ui.lesson_info)

        # Get lessons from the database
        app_state = app_state_ref(self)
        lessons = json.loads(app_state.api_get('/lessons').content)
        # Filter out all lessons that haven't occurred yet
        past_lessons = list(filter(lambda x: x['dateTime'] < time_ms(), lessons))
        # Sort the past lessons so that the most recent is first in the list
        past_lessons.sort(key=lambda x: x['dateTime'], reverse=True)

        # Create the lesson info form using the last lesson
        self.ui.lesson_info = LessonInfoForm(self, past_lessons[0])
        self.ui.lesson_info_layout.addWidget(self.ui.lesson_info)
