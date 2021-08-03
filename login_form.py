from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QEvent, Qt
from ui.login_ui import Ui_Login
from utils import app_state_ref, show_message_box


class LoginForm(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.ui = Ui_Login()
        self.ui.setupUi(self)

        self.ui.login_button.clicked.connect(self.login)
        self.ui.goto_register_button.clicked.connect(self.goto_register)
        self.installEventFilter(self)

        self.ui.address_txt.setText('localhost')
        self.ui.port_txt.setText('3000')

    def login(self):
        # Store all the user input in a dictionary
        fields = {}
        fields['username'] = self.ui.username_txt.text()
        fields['password'] = self.ui.password_txt.text()
        fields['address'] = self.ui.address_txt.text()
        fields['port'] = self.ui.port_txt.text()

        # Make sure every field has been filled out.
        if '' in fields.values():
            show_message_box(
                'User input error',
                'One or more fields have been left blank. Please try again.')
            return

        # Pass the input to ApplicationState instance
        app_state = app_state_ref(self)
        app_state.set_server(fields['address'], fields['port'])
        # Attempt to log in, and display a message if it fails
        try:
            # False means wrong password
            if not app_state.set_user(fields['username'], fields['password']):
                show_message_box(
                    'Invalid Credentials',
                    'The provided username or password is incorrect.')
                self.ui.password_txt.clear()
                return
        except:
            # Exception means connection failed or another error
            show_message_box(
                'An error occurred',
                'Something went wrong, check your connection to the server')
            return

        show_message_box('User Details', f'''
        Username: {app_state.username}
        Full Name: {app_state.fullname}
        Account Type: {app_state.account_type}
        ''')
        if app_state.account_type == 'teacher':
            self.window().setup_teacher_pages()
            parent = self.parent()
            parent.setCurrentWidget(parent.students_form)

    def set_server(self, address, port):
        self.ui.address_txt.setText(address)
        self.ui.port_txt.setText(port)

    def goto_register(self):
        parent = self.parent()
        parent.register_form.set_server(
            self.ui.address_txt.text(), self.ui.port_txt.text())
        parent.setCurrentWidget(parent.register_form)

    def eventFilter(self, widget, event):
        # If enter key was pressed, call the login code
        if event.type() == QEvent.KeyPress:
            key = event.key()
            if key == Qt.Key_Enter or key == Qt.Key_Return:
                self.login()
                return True
            
        # If not, pass the event on to the default handler
        return super().eventFilter(widget, event)

    def showEvent(self, event):
        # Reset fields when login form becomes visible
        self.ui.username_txt.clear()
        self.ui.password_txt.clear()
        self.ui.username_txt.setFocus()
