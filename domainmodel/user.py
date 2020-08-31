from typing import List

from domainmodel.movie import Movie
from domainmodel.review import Review


class User:

    def __init__(self, user_name: str, password: str):
        if type(user_name) is not str or user_name == "":
            self.__user_name = None
        else:
            self.__user_name = user_name.lower().strip()

        if type(password) is not str or password == "":
            self.__password = None
        else:
            self.__password = password.strip()

        self.__watched_movies = []
        self.__reviews = []
        self.__time_spent_watching_movies_minutes = 0

    @property
    def user_name(self) -> str:
        return self.__user_name

    @property
    def password(self) -> str:
        return self.__password

    @property
    def watched_movies(self) -> List[Movie]:
        return self.__watched_movies

    @property
    def reviews(self) -> List[Review]:
        return self.__reviews

    @property
    def time_spent_watching_movies_minutes(self) -> int:
        return self.__time_spent_watching_movies_minutes

    @time_spent_watching_movies_minutes.setter
    def time_spent_watching_movies_minutes(self, time_spent):
        if type(time_spent) is int and time_spent >= 0:
            self.__time_spent_watching_movies_minutes = time_spent

    def __repr__(self):
        return f"<User {self.__user_name}>"

    def __eq__(self, other):
        return self.__user_name == other.__user_name

    def __lt__(self, other):
        return self.__user_name < other.__user_name

    def __hash__(self):
        return hash(self.__user_name)

    def watch_movie(self, movie):
        if type(movie) is Movie and movie not in self.__watched_movies:
            self.__watched_movies.append(movie)
            self.__time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review):
        if type(review) is Review and review not in self.__reviews:
            self.__reviews.append(review)


class TestUserMethods:

    def test_init(self):
        user1 = User('Martin', 'pw12345')
        assert user1.user_name == 'martin'
        assert user1.password == 'pw12345'
        user2 = User('', 'pw67890')
        assert user2.user_name is None
        assert user2.password == 'pw67890'
        user3 = User('Daniel', 12345)
        assert user3.user_name == 'daniel'
        assert user3.password is None

    def test_time_spent(self):
        user1 = User('Martin', 'pw12345')
        user1.time_spent_watching_movies_minutes = 100
        assert user1.time_spent_watching_movies_minutes == 100
        user2 = User('Ian', 'pw67890')
        user2.time_spent_watching_movies_minutes = -100
        assert user2.time_spent_watching_movies_minutes == 0

    def test_watch_movie(self):
        user = User('Martin', 'pw12345')

        movie1 = Movie('Moana', 2016)
        movie1.runtime_minutes = 113

        movie2 = Movie('Frozen', 2014)
        movie2.runtime_minutes = 109

        user.watch_movie(movie1)
        assert len(user.watched_movies) == 1
        assert user.watched_movies[0] == movie1
        assert user.time_spent_watching_movies_minutes == 113

        user.watch_movie(movie2)
        assert len(user.watched_movies) == 2
        assert user.watched_movies[1] == movie2
        assert user.time_spent_watching_movies_minutes == 222

        user.watch_movie(movie1)
        assert len(user.watched_movies) == 2
        assert user.time_spent_watching_movies_minutes == 222

    def test_add_review(self):
        user = User('Martin', 'pw12345')
        movie1 = Movie('Moana', 2016)
        review1 = Review(movie1, 'I liked it', 10)
        movie2 = Movie('Frozen', 2014)
        review2 = Review(movie2, 'I did not like it', 1)
        review3 = review1

        user.add_review(review1)
        assert len(user.reviews) == 1
        assert user.reviews[0] == review1

        user.add_review(review2)
        assert len(user.reviews) == 2
        assert user.reviews[1] == review2

        user.add_review(review3)
        assert len(user.reviews) == 2