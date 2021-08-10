import json
from PySide6.QtWidgets import QWidget
from ui.student_dashboard_ui import Ui_StudentDashboard
from utils import app_state_ref

class StudentDashboard(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.ui = Ui_StudentDashboard()
        self.ui.setupUi(self)

    def setup(self):
      pass
