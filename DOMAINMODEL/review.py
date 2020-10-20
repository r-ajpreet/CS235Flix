from datetime import datetime

from DOMAINMODEL.movie import Movie

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

    def __repr__(self):
        return f"Review: {self.__review_text}\nRating: {self.__rating}"

    def __eq__(self, other):
        return (self.__movie == other.__movie and
                self.__review_text == other.__review_text and
                self.__rating == other.__rating and
                self.__timestamp == other.__timestamp)


class TestReviewMethods:

    def test_init(self):
        movie1 = Movie("Moana", 2016)
        review_text1 = "This movie was very enjoyable."
        rating1 = 8
        review1 = Review(movie1, review_text1, rating1)
        assert review1.movie == movie1
        assert review1.review_text == review_text1
        assert review1.rating == rating1

        movie2 = ""
        review_text2 = ""
        rating2 = ""
        review2 = Review(movie2, review_text2, rating2)
        assert review2.movie is None
        assert review2.review_text is None
        assert review2.rating is None

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