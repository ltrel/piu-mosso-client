import requests
from PySide6.QtWidgets import QWidget, QMessageBox
from ui.register_ui import Ui_Register


class RegisterForm(QWidget):
    def __init__(self, parent):
        super(RegisterForm, self).__init__(parent)

        self.ui = Ui_Register()
        self.ui.setupUi(self)

        self.ui.register_button.clicked.connect(self.register)
        self.ui.goto_login_button.clicked.connect(self.goto_login)

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
        if('' in fields.values()):
            message_box = QMessageBox()
            message_box.setWindowTitle('User input error')
            message_box.setText(
                'One or more fields have been left blank. Please try again.')
            message_box.show()
            self.ui.verify_password_txt.clear()
            return

        # Make sure the two passwords are the same.
        if(fields['password'] != fields['verify_password']):
            message_box = QMessageBox()
            message_box.setWindowTitle('User input error')
            message_box.setText(
                'The passwords entered do not match. Please try again.')
            message_box.exec()
            self.ui.password_txt.clear()
            self.ui.verify_password_txt.clear()
            return

        # Send the request to the server.
        res = requests.post(f'http://{fields["address"]}:{fields["port"]}/register', json={
            'username': fields['username'],
            'fullName': fields['fullname'],
            'password': fields['password'],
            'type': fields['account_type']
        })

        print(res)

    def set_server(self, address, port):
        self.ui.address_txt.setText(address)
        self.ui.port_txt.setText(port)

    def goto_login(self):
        parent = self.parent()
        parent.login_form.set_server(
            self.ui.address_txt.text(), self.ui.port_txt.text())
        parent.setCurrentWidget(parent.login_form)
