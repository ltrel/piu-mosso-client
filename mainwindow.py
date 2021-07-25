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
        self.ui.stackedWidget = QStackedWidget() 
        self.ui.stackedWidget.setObjectName('stackedWidget')
        self.ui.stackedWidget.register_form = RegisterForm(None)
        self.ui.stackedWidget.login_form = LoginForm(None)
        self.ui.stackedWidget.addWidget(self.ui.stackedWidget.register_form)
        self.ui.stackedWidget.addWidget(self.ui.stackedWidget.login_form)
        # Add it to the top level layout
        self.ui.gridLayout.addWidget(self.ui.stackedWidget)
