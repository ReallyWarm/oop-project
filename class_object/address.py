class Address:
    def __init__(self, name:str, company:str, country:str, state:str,
                 city:str, address:str, phone_number:str, postal_code:str) -> None:
        self._name = name
        self._company = company
        self._country = country
        self._state = state
        self._city = city
        self._address = address
        self._phone_number = phone_number
        self._postal_code = postal_code
 
    @property
    def name(self) -> str:
        return self._name 
    
    @property
    def country(self) -> str:
        return self._country
    
    @property
    def state(self) -> str:
        return self._state
    
    @property
    def city(self) -> str:
        return self._city
    
    @property
    def address(self) -> str:
        return self._address

    def edit_address(self, name:str=None, company:str=None, country:str=None, state:str=None, city:str=None ,address:str=None, phone_number:str=None, postal_code:str=None) -> None:
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