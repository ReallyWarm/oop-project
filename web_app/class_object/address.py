
# manage the address


class Address:
    def __init__(self, name, company, country,
                 state, city, address, phone_number, postal_code) -> None:
        self._name = name
        self._company = company
        self._country = country
        self._state = state
        self._city = city
        self._address = address
        self._phone_number = phone_number
        self._postal_code = postal_code

    
    def get_address(self,name,company,country,state,city,address,phone_number,postal_code):
        return Address(name,company,country,state,city,address,phone_number,postal_code)

    def update_address(self):
        return print('Address has updated')

    def edit_address(self, name, company, country, state, city , address, phone_number, postal_code):
        if  Address(name,company,country,state,city,address,phone_number,postal_code)._name == self._name:
            self._name = name
            self._company = company
            self._country = country
            self._state = state
            self._city = city
            self._address = address
            self._phone_number = phone_number
            self._postal_code = postal_code
        
    def __repr__(self) -> str:
        return "{}".format(self._name +','+"{}".format(self._company)+','+"{}".format(self._country)+','+"{}".format(self._state)+
                           ','+"{}".format(self._city)+','+"{}".format(self._phone_number)+
                           ','+"{}".format(self._address)+','+"{}".format(self._phone_number)+','+"{}".format(self._postal_code))