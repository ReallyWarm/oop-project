class Payment : 
    def __init__(self, total_amount:float, date_create:str, id:str, status:str) -> None:
        self.total_amount = total_amount
        self.date_creat = date_create
        self.status = status
        self.id = id

    def make_payment(self):
        pass

    def perform_payment(self):
        pass