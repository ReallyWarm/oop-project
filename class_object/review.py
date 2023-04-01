class Review():
    def __init__(self, user_name:str, head_of_review:str, comment:str, date_of_review:str, rating:float) -> None:
        self._user_name = user_name
        self._head_of_review = head_of_review
        self._rating = rating
        self._comment = comment
        self._date_of_review = date_of_review

    def __str__(self) -> str:
        return "Now in review object \n username: {} \n head of review: {} \n \
            rating: {} \n comment: {} \n date of review: {}"\
                .format(self._user_name, self._head_of_review, self._rating, self._comment, self._date_of_review)
    
    def __repr__(self) -> str:
        return "{}".format(self._head_of_review)
