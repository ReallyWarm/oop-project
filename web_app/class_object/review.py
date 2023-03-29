class Review():
    def __init__(self, user_name, head_of_review, comment, date_of_review) -> None:
        self._user_name = user_name
        self._head_of_review = head_of_review
        self._rating = 0.00
        self._comment = comment
        self._date_of_review = date_of_review

    def get_reviews(self,user_name,head_of_review,comment,date_of_review):
        self._reviews = Review(user_name,head_of_review,comment,date_of_review)
        return self._reviews
        