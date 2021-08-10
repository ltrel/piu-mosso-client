from PySide6.QtWidgets import QWidget, QPushButton
from ui.teacher_sidebar_ui import Ui_TeacherSidebar
from utils import app_state_ref


class TeacherSidebar(QWidget):
    def __init__(self, parent, selected_button=''):
        super().__init__(parent)

        self.ui = Ui_TeacherSidebar()
        self.ui.setupUi(self)

        # Highlight the button for the current application page
        self.selected_button = self.findChild(QPushButton, selected_button)
        if self.selected_button != None:
            self.selected_button.setStyleSheet('background-color: blue')

        self.ui.new_button.clicked.connect(self.buttons_handler)
        self.ui.last_button.clicked.connect(self.buttons_handler)
        self.ui.calendar_button.clicked.connect(self.buttons_handler)
        self.ui.students_button.clicked.connect(self.buttons_handler)
        self.ui.files_button.clicked.connect(self.buttons_handler)

        self.ui.sign_out_button.clicked.connect(self.sign_out)

    def buttons_handler(self):
        stacked_widget = self.window().ui.stacked_widget
        sender = self.sender()
        # If already on the right page, do nothing
        if sender == self.selected_button:
            return
        button_name = sender.objectName()
        # Check which button was pressed and go to the relevant page
        if button_name == 'new_button':
            stacked_widget.new_lesson_form.setup()
            stacked_widget.setCurrentWidget(stacked_widget.new_lesson_form)
        elif button_name == 'last_button':
            stacked_widget.last_lesson_form.setup()
            stacked_widget.setCurrentWidget(stacked_widget.last_lesson_form)
        elif button_name == 'calendar_button':
            stacked_widget.calendar_form.setup()
            stacked_widget.setCurrentWidget(stacked_widget.calendar_form)
        elif button_name == 'students_button':
            stacked_widget.students_form.setup()
            stacked_widget.setCurrentWidget(stacked_widget.students_form)
        elif button_name == 'files_button':
            stacked_widget.files_form.setup()
            stacked_widget.setCurrentWidget(stacked_widget.files_form)
            pass
        else:
            raise Exception('Unexpected button pressed')

    def sign_out(self):
        stacked_widget = self.window().ui.stacked_widget
        stacked_widget.login_form.setup()
        stacked_widget.setCurrentWidget(stacked_widget.login_form)

    def showEvent(self, event):
        name = app_state_ref(self).fullname
        self.ui.user_label.setText(f'You are signed in as:\n{name}')
