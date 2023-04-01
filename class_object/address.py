
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
 
    @property
    def name(self):
        return self._name 
    
    @property
    def country(self):
        return self._country
    
    @property
    def state(self):
        return self._state
    
    @property
    def city(self):
        return self._city
    
    @property
    def address(self):
        return self._address
    
    def get_address(self):
        pass

    def update_address(self):
        pass

    def edit_address(self, name=None, company=None, country=None, state=None, city=None , address=None, phone_number=None, postal_code=None):
        if name is not None :
            self._name = name
        if company is not None :
            self._company = company
        if country is not None :
            self._country = country
        if state is not None :
            self._state = state
        if city is not None :
            self._city = city
        if address is not None :
            self._address = address
        if phone_number is not None :
            self._phone_number = phone_number
        if postal_code is not None :
            self._postal_code = postal_code

            
    def __repr__(self) -> str:
        return "{}".format(self._name +','+"{}".format(self._company)+','+"{}".format(self._country)+','+"{}".format(self._state)+
                           ','+"{}".format(self._city)+','+"{}".format(self._address)+','+"{}".format(self._phone_number)+','+"{}".format(self._postal_code))