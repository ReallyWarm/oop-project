class Address:
    def __init__(self, first_name, last_name, email, company, country, /
                 state, city, address, phone_number, postal_code) -> None:
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._company = company
        self._country = country
        self._state = state
        self._city = city
        self._address = address
        self._phone_number = phone_number
        self._postal_code = postal_code
