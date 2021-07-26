from PySide6.QtWidgets import QWidget, QMainWindow, QStackedWidget
from ui.mainwindow_ui import Ui_MainWindow
from register_form import RegisterForm
from login_form import LoginForm

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Create stacked widget to store the application pages
        self.ui.stacked_widget = QStackedWidget() 
        self.ui.stacked_widget.setObjectName('stacked_widget')
        self.ui.stacked_widget.register_form = RegisterForm(None)
        self.ui.stacked_widget.login_form = LoginForm(None)
        self.ui.stacked_widget.addWidget(self.ui.stacked_widget.register_form)
        self.ui.stacked_widget.addWidget(self.ui.stacked_widget.login_form)
        # Add it to the top level layout
        self.ui.grid_layout.addWidget(self.ui.stacked_widget)
