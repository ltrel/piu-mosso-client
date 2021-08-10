from PySide6.QtWidgets import QMainWindow, QStackedWidget
from ui.mainwindow_ui import Ui_MainWindow
from register_form import RegisterForm
from login_form import LoginForm
from application_state import ApplicationState
from students_form import StudentsForm
from new_lesson_form import NewLessonForm
from last_lesson_form import LastLessonForm
from calendar_form import CalendarForm
from files_form import FilesForm


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.app_state = ApplicationState()

        # Create stacked widget to store the application pages
        self.ui.stacked_widget = QStackedWidget()
        self.ui.stacked_widget.setObjectName('stacked_widget')
        self.ui.grid_layout.addWidget(self.ui.stacked_widget)

        self.ui.stacked_widget.register_form = RegisterForm(self.ui.stacked_widget)
        self.ui.stacked_widget.login_form = LoginForm(self.ui.stacked_widget)
        self.ui.stacked_widget.students_form = StudentsForm(self.ui.stacked_widget)
        self.ui.stacked_widget.new_lesson_form = NewLessonForm(self.ui.stacked_widget)
        self.ui.stacked_widget.last_lesson_form = LastLessonForm(self.ui.stacked_widget)
        self.ui.stacked_widget.calendar_form = CalendarForm(self.ui.stacked_widget)
        self.ui.stacked_widget.files_form = FilesForm(self.ui.stacked_widget)

        self.ui.stacked_widget.addWidget(self.ui.stacked_widget.register_form)
        self.ui.stacked_widget.addWidget(self.ui.stacked_widget.login_form)
        self.ui.stacked_widget.addWidget(self.ui.stacked_widget.students_form)
        self.ui.stacked_widget.addWidget(self.ui.stacked_widget.new_lesson_form)
        self.ui.stacked_widget.addWidget(self.ui.stacked_widget.last_lesson_form)
        self.ui.stacked_widget.addWidget(self.ui.stacked_widget.calendar_form)
        self.ui.stacked_widget.addWidget(self.ui.stacked_widget.files_form)

        self.ui.stacked_widget.setCurrentWidget(self.ui.stacked_widget.login_form)
    
    def setup_teacher_pages(self):
        self.ui.stacked_widget.students_form.setup()
        self.ui.stacked_widget.new_lesson_form.setup()
