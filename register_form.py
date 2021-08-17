import requests
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QEvent, Qt
from ui.register_ui import Ui_Register
from utils import show_message_box


class RegisterForm(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.ui = Ui_Register()
        self.ui.setupUi(self)
        self.setup()

        self.ui.register_button.clicked.connect(self.register)
        self.ui.goto_login_button.clicked.connect(self.goto_login)
        self.installEventFilter(self)


    def register(self):
        # Store all the user input in a dictionary
        fields = {}
        fields['username'] = self.ui.username_txt.text()
        fields['fullname'] = self.ui.fullname_txt.text()
        fields['password'] = self.ui.password_txt.text()
        fields['verify_password'] = self.ui.verify_password_txt.text()
        fields['account_type'] = 'student' if self.ui.student_button.isChecked(
        ) else 'teacher'
        fields['address'] = self.ui.address_txt.text()
        fields['port'] = self.ui.port_txt.text()

        # Make sure every field has been filled out.
        if '' in fields.values():
            show_message_box(
                'User input error',
                'One or more fields have been left blank. Please try again.')
            return

        # Make sure the two passwords are the same.
        if fields['password'] != fields['verify_password']:
            show_message_box(
                'User input error',
                'The passwords entered do not match. Please try again.')
            self.ui.password_txt.clear()
            self.ui.verify_password_txt.clear()
            return

        # Send the request to the server.
        res = None
        try:
            res = requests.post(f'http://{fields["address"]}:{fields["port"]}/register', json={
                'username': fields['username'],
                'fullName': fields['fullname'],
                'password': fields['password'],
                'type': fields['account_type']
            })
        # Handle connection error
        except:
            show_message_box(
                'An error occurred',
                'Something went wrong, check your connection to the server')
        # Handle username conflict.
        if res.status_code == 409:
            show_message_box(
                'Username Taken',
                'A user acount with that username already exists'
            )
            self.setup()
            return
        
        show_message_box(
            'Success',
            'Account created succesfully, proceed to the login page'
        )
        self.setup()

    def set_server(self, address, port):
        self.ui.address_txt.setText(address)
        self.ui.port_txt.setText(port)

    def goto_login(self):
        parent = self.parent()
        parent.login_form.setup()
        parent.login_form.set_server(
            self.ui.address_txt.text(), self.ui.port_txt.text())
        parent.setCurrentWidget(parent.login_form)

    def eventFilter(self, widget, event):
        # If enter key was pressed, call the login code
        if event.type() == QEvent.KeyPress:
            key = event.key()
            if key == Qt.Key_Enter or key == Qt.Key_Return:
                self.register()
                return True
            
        # If not, pass the event on to the default handler
        return super().eventFilter(widget, event)

    def setup(self):
        # Reset fields when login form becomes visible
        self.ui.username_txt.clear()
        self.ui.fullname_txt.clear()
        self.ui.password_txt.clear()
        self.ui.verify_password_txt.clear()
        self.ui.student_button.setChecked(True)
        self.ui.username_txt.setFocus()
