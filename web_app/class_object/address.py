class Address:
    def __init__(self, name, company, country, /
                 state, city, address, phone_number, postal_code) -> None:
        self._name = name
        self._company = company
        self._country = country
        self._state = state
        self._city = city
        self._address = address
        self._phone_number = phone_number
        self._postal_code = postal_code

    def get_address(self):
        pass

    def edit_address(self):
        pass

    def update_address(self):
        pass

    def delete_address(self):
        pass