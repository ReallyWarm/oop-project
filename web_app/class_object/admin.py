class Admin:
    def __init__(self, first_name, last_name, email) -> None:
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._server_coupon = [ ]