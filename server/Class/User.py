class User:
    def __init__(self, adresse, user_name):
        self._adresse = adresse
        self._user_name = user_name

    def get_adresse(self):
        return self._adresse

    def get_user_name(self):
        return self._user_name
