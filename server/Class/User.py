class User:
    def __int__(self, ip, port, user_name):
        self._ip = ip
        self._port = port
        self._user_name = user_name

    def get_ip(self):
        return self._ip

    def get_port(self):
        return self._port

    def get_user_name(self):
        return self._user_name

