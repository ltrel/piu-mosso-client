from PySide6.QtWidgets import QWidget
from ui.lesson_info_ui import Ui_LessonInfoForm
from utils import app_state_ref


class LessonInfoForm(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.ui = Ui_LessonInfoForm()
        self.ui.setupUi(self)
