class Tool:
    def __init__(self, code, name, description, brand, \
                 amount, image, price, type_of_tool) -> None:
          self._code = code
          self._name = name
          self._description = description
          self._brand = brand
          self._amount = amount
          self._price = price
          self._category = type_of_tool
          self._reviews = [ ]
          self._image = [image]
          self._wholesale = [ ]
          self._rating = 0.00
          self.__n_review = 0.00
          self.__rated_review = 0.00

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price
    
    def get_attributes(self, attr):
        return self.__dict__[attr]

    def modify_tool(self):
        print(self)
        a = input('Choose modify infomation: \n 1 = name \n 2 = description \n 3 = brand \n 4 = price \n your input:::')

        def modify_name(new_name):
            self._name = new_name
        def modify_description(new_description):
            self._description = new_description
        def modify_brand(new_brand):
            self._brand = new_brand
        def modify_price(new_price):
            self._price = new_price
        # print(a)  
        if (int(a) == 1):
            new_name = input('Enter new name:')
            modify_name(new_name)
            print('changing success')
        elif ( int(a) == 2 ):
            new_description = input('Enter new description:')
            modify_description(new_description)
            print('changing success')
        elif (int(a) == 3 ):
            new_brand = input('Enter new brand:')
            modify_brand(new_brand)
            print('changing success')
        elif (int(a) == 4):
            new_price = input('Enter new price:')
            modify_price(new_price)
            print('changing success')
        print(self)

    def add_review(self, review):
        self.get_review_list.append(review)
        print(self.get_review_list)
        self.__n_review += 1
        self.__rated_review += review._rating
        self._rating = self.__rated_review / self.__n_review
        print("Now rating is {}".format(self.get_rating))
        print("update review success")

    @property
    def get_review_list(self):
        return self._reviews
    @property
    def get_rating(self):
        return self._rating

    def __str__(self) -> str:
        return str(self.__class__)+'\n'+', '.join(f'{key} : {value}' for key, value in self.__dict__.items())

class Item:
    def __init__(self, tool, buy_amount) -> None: 
        self._tool = tool
        self._buy_amount = buy_amount
        self._items_price = tool.price * buy_amount

    @property
    def tool(self):
        return self._tool
    
    def set_amount(self):
        pass

    def update_item(self):
        pass