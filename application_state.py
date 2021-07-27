import datetime
import json
import requests

class ApplicationState():
    def __init__(self):
        self.server_address = None
        self.server_port = None

        self.username = None
        self.fullname = None
        self.password = None
        self.account_type = None

        self.__auth_token = None
        self.__token_expiry_date = None

    def set_server(self, address, port):
        self.server_address = address
        self.server_port = port

    def set_user(self, username, password):
        # Set basic user details
        self.username = username
        self.password = password

        # Try to fetch an authentication token from the server
        try:
            self.__set_token()
        except:
            return False

        # Verify the token and get the user's details
        verify_url = self.get_api_url('/verify-token')
        query = {'auth_token': self.get_token()}
        res = requests.get(verify_url, params=query)
        if res.status_code != 200:
            return Exception('Token not valid')
        user_details = json.loads(res.content)

        # Set the rest of the user's details
        self.fullname = user_details['fullName']
        self.account_type = user_details['accountType']
        return True

    def get_api_url(self, endpoint):
        if not(self.server_address and self.server_port):
            raise ValueError('Server details not set')

        base_url = f'http://{self.server_address}:{self.server_port}'
        return base_url + endpoint

    def get_token(self):
        # Regenerate token if it's too old
        if datetime.datetime.now() >= self.__token_expiry_date:
            self.__set_token()
        
        return self.__auth_token

    def __set_token(self):
        # Get token from login route
        login_url = self.get_api_url('/login')
        body = { 'username': self.username, 'password': self.password }
        res = requests.post(login_url, json=body)
        if res.status_code != 200:
            raise Exception('Login failed')

        # Calculate expiry date and save token
        self.__auth_token = json.loads(res.content)['token']
        now = datetime.datetime.now()
        offset = datetime.timedelta(hours=1)
        self.__token_expiry_date = now + offset
