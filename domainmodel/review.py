from datetime import datetime

from domainmodel.movie import Movie


class Review:

    def __init__(self, movie: Movie, review_text: str, rating: int):
        if type(movie) is Movie:
            self.__movie = movie
        else:
            self.__movie = None

        if type(review_text) is not str or review_text == "":
            self.__review_text = None
        else:
            self.__review_text = review_text

        if type(rating) is int and 0 < rating < 11:
            self.__rating = rating
        else:
            self.__rating = None

        self.__timestamp = datetime.now()

        # user who wrote review - in later Q
        # self.__user = None

    @property
    def movie(self) -> Movie:
        return self.__movie

    @property
    def review_text(self) -> str:
        return self.__review_text

    @property
    def rating(self) -> int:
        return self.__rating

    @property
    def timestamp(self) -> datetime:
        return self.__timestamp

    # @property
    # def user(self) -> User:
    #     return self.__user

    def __repr__(self):
        return f"Review: {self.__review_text}\nRating: {self.__rating}"

    def __eq__(self, other):
        return (self.__movie == other.__movie and
                self.__review_text == other.__review_text and
                self.__rating == other.__rating and
                self.__timestamp == other.__timestamp)


class TestReviewMethods:

    def test_init(self):
        movie = Movie("Moana", 2016)
        review_text = "This movie was very enjoyable."
        rating = 8
        review = Review(movie, review_text, rating)
        assert review.movie == movie
        assert review.review_text == review_text
        assert review.rating == rating

    def test_repr(self):
        movie = Movie("Moana", 2016)
        review_text = "This movie was very enjoyable."
        rating = 8
        review = Review(movie, review_text, rating)
        assert review.__repr__() == "Review: This movie was very enjoyable.\nRating: 8"

    def test_eq(self):
        movie1 = Movie("Moana", 2016)
        movie2 = Movie("Frozen", 2014)
        review_text = "This movie was very enjoyable."
        rating = 8
        review1 = Review(movie1, review_text, rating)
        review2 = Review(movie2, review_text, rating)
        review3 = Review(movie1, review_text, rating)
        review4 = review1
        assert review1.__eq__(review2) is False
        assert review1.__eq__(review3) is False
        assert review1.__eq__(review4) is True
