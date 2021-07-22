import requests
from PySide6.QtWidgets import QWidget, QMessageBox
from ui.login_ui import Ui_Login


class LoginForm(QWidget):
    def __init__(self, parent):
        super(LoginForm, self).__init__(parent)

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
        if('' in fields.values()):
            message_box = QMessageBox()
            message_box.setWindowTitle('User input error')
            message_box.setText(
                'One or more fields have been left blank. Please try again.')
            message_box.show()
            self.ui.verify_password_txt.clear()
            return

        # Send the request to the server.
        res = requests.post(f'http://{fields["address"]}:{fields["port"]}/login', json={
            'username': fields['username'],
            'password': fields['password'],
        })

        print(res)

    def goto_register(self):
        from register_form import RegisterForm
        self.parent().setCentralWidget(RegisterForm(None))
