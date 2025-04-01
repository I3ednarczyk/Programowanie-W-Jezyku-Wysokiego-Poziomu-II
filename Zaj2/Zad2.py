class UserNotFoundError(Exception):
    pass


class WrongPasswordError(Exception):
    pass


class UserAuth:
    def __init__(self, users=None):
        self.users = users if users else {}

    def register(self, username, password):
        self.users[username] = password

    def login(self, username, password):
        if username not in self.users:
            raise UserNotFoundError("Użytkownik nie istnieje.")
        if self.users[username] != password:
            raise WrongPasswordError("Niepoprawne hasło.")
        return "Logowanie powiodło się!"

auth = UserAuth({"admin": "1234", "user": "abcd"})
try:
    auth.login("admin", "1234")  # Sukces
    auth.login("unknown", "pass")  # Powinien rzucić UserNotFoundError
    auth.login("user", "wrongpass")  # Powinien rzucić WrongPasswordError
except Exception as e:
    print(f"Błąd: {e}")