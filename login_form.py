from PySide6.QtWidgets import QWidget, QMessageBox, QApplication
from ui.login_ui import Ui_Login


class LoginForm(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.ui = Ui_Login()
        self.ui.setupUi(self)

        self.ui.login_button.clicked.connect(self.login)
        self.ui.goto_register_button.clicked.connect(self.goto_register)

    def login(self):
        # Store all the user input in a dictionary
        fields = {}
        fields['username'] = self.ui.username_txt.text()
        fields['password'] = self.ui.password_txt.text()
        fields['address'] = self.ui.address_txt.text()
        fields['port'] = self.ui.port_txt.text()

        # Make sure every field has been filled out.
        if '' in fields.values():
            message_box = QMessageBox()
            message_box.setWindowTitle('User input error')
            message_box.setText(
                'One or more fields have been left blank. Please try again.')
            message_box.exec()
            return

        app_state = QApplication.topLevelWidgets()[0].app_state
        app_state.set_server(fields['address'], fields['port'])
        if not app_state.set_user(fields['username'], fields['password']):
            message_box = QMessageBox()
            message_box.setWindowTitle('Invalid Credentials')
            message_box.setText(
                'The provided username or password is incorrect.')
            message_box.exec()
            self.ui.password_txt.clear()
            return

        message_box = QMessageBox()
        message_box.setWindowTitle('User Details')
        message_box.setText(f'''
        Username: {app_state.username}
        Full Name: {app_state.fullname}
        Account Type: {app_state.account_type}
        ''')
        message_box.exec()

    def set_server(self, address, port):
        self.ui.address_txt.setText(address)
        self.ui.port_txt.setText(port)

    def goto_register(self):
        parent = self.parent()
        parent.register_form.set_server(
            self.ui.address_txt.text(), self.ui.port_txt.text())
        parent.setCurrentWidget(parent.register_form)
