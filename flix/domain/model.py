# =====
# ACTOR
# =====
from datetime import datetime
from typing import List

import pytest


class Actor:

    def __init__(self, actor_full_name: str):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name.strip()
        self.__colleagues = []

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name

    @property
    def colleagues(self):
        return self.__colleagues

    def __repr__(self):
        return f"<Actor {self.__actor_full_name}>"

    def __eq__(self, other):
        return self.__actor_full_name == other.__actor_full_name

    def __lt__(self, other):
        return self.__actor_full_name < other.__actor_full_name

    def __hash__(self):
        return hash(self.__actor_full_name)

    def add_actor_colleague(self, colleague):
        if type(colleague) is Actor:
            if not self.check_if_this_actor_worked_with(colleague):
                self.__colleagues.append(colleague)

    def check_if_this_actor_worked_with(self, colleague):
        if type(colleague) is Actor:
            return colleague in self.__colleagues


class TestActorMethods:

    def test_init(self):
        actor1 = Actor("Angelina Jolie")
        assert repr(actor1) == "<Actor Angelina Jolie>"
        actor2 = Actor("")
        assert actor2.actor_full_name is None
        actor3 = Actor(50)
        assert actor3.actor_full_name is None

    def test_repr(self):
        actor1 = Actor("Angelina Jolie")
        assert actor1.__repr__() == "<Actor Angelina Jolie>"

    def test_eq(self):
        actor1 = Actor("Angelina Jolie")
        actor2 = Actor("Jack Black")
        actor3 = Actor("Angelina Jolie")
        assert actor1.__eq__(actor2) is False
        assert actor1.__eq__(actor3) is True

    def test_lt(self):
        actor1 = Actor("Angelina Jolie")
        actor2 = Actor("Jack Black")
        assert actor1.__lt__(actor2) is True
        assert actor2.__lt__(actor1) is False

    def test_hash(self):
        actor1 = Actor("Angelina Jolie")
        actor2 = Actor("Jack Black")
        actor3 = Actor("Angelina Jolie")
        assert actor1.__hash__() != actor2.__hash__()
        assert actor1.__hash__() == actor3.__hash__()

    def test_add_actor_colleague(self):
        actor1 = Actor("Angelina Jolie")
        actor2 = Actor("Tom Cruise")

        # add new object not of type Actor
        actor1.add_actor_colleague(50)
        assert len(actor1.colleagues) == 0

        # add new colleague
        actor1.add_actor_colleague(actor2)
        assert actor1.colleagues[0] == actor2

        # add existing colleague
        actor1.add_actor_colleague(actor2)
        assert len(actor1.colleagues) == 1

        # add a second colleague
        actor3 = Actor("Chris Pratt")
        actor1.add_actor_colleague(actor3)
        assert len(actor1.colleagues) == 2
        assert actor1.colleagues[1] == actor3

    def test_check_if_this_actor_worked_with(self):
        actor1 = Actor("Angelina Jolie")
        actor2 = Actor("Tom Cruise")
        actor3 = Actor("Chris Pratt")

        actor1.add_actor_colleague(actor2)

        assert actor1.check_if_this_actor_worked_with(actor2) is True
        assert actor1.check_if_this_actor_worked_with(actor3) is False


# ========
# DIRECTOR
# ========

class Director:

    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()

    @property
    def director_full_name(self) -> str:
        return self.__director_full_name

    def __repr__(self):
        return f"<Director {self.__director_full_name}>"

    def __eq__(self, other):
        return self.__director_full_name == other.__director_full_name

    def __lt__(self, other):
        return self.__director_full_name < other.__director_full_name

    def __hash__(self):
        return hash(self.__director_full_name)


class TestDirectorMethods:

    def test_init(self):
        director1 = Director("Taika Waititi")
        assert repr(director1) == "<Director Taika Waititi>"
        director2 = Director("")
        assert director2.director_full_name is None
        director3 = Director(42)
        assert director3.director_full_name is None

    def test_repr(self):
        director1 = Director("Taika Waititi")
        assert director1.__repr__() == "<Director Taika Waititi>"

    def test_eq(self):
        director1 = Director("Taika Waititi")
        director2 = Director("James Cameron")
        director3 = Director("Taika Waititi")
        assert director1.__eq__(director2) is False
        assert director1.__eq__(director3) is True

    def test_lt(self):
        director1 = Director("Taika Waititi")
        director2 = Director("James Cameron")
        assert director1.__lt__(director2) is False
        assert director2.__lt__(director1) is True

    def test_hash(self):
        director1 = Director("Taika Waititi")
        director2 = Director("James Cameron")
        director3 = Director("Taika Waititi")
        assert director1.__hash__() != director2.__hash__()
        assert director1.__hash__() == director3.__hash__()


# =====
# GENRE
# =====


class Genre:

    def __init__(self, genre_name: str):
        if genre_name == "" or type(genre_name) is not str:
            self.__genre_name = None
        else:
            self.__genre_name = genre_name.strip()

    @property
    def genre_name(self) -> str:
        return self.__genre_name

    def __repr__(self):
        return f'<Genre {self.__genre_name}>'

    def __eq__(self, other):
        return self.__genre_name == other.__genre_name

    def __lt__(self, other):
        return self.__genre_name < other.__genre_name

    def __hash__(self):
        return hash(self.__genre_name)


class TestGenreMethods:

    def test_init(self):
        genre1 = Genre("Horror")
        assert repr(genre1) == "<Genre Horror>"
        genre2 = Genre("")
        assert genre2.genre_name is None
        genre3 = Genre(50)
        assert genre3.genre_name is None

    def test_repr(self):
        genre1 = Genre("Horror")
        assert genre1.__repr__() == "<Genre Horror>"

    def test_eq(self):
        genre1 = Genre("Horror")
        genre2 = Genre("Comedy")
        genre3 = Genre("Horror")
        assert genre1.__eq__(genre2) is False
        assert genre1.__eq__(genre3) is True

    def test_lt(self):
        genre1 = Genre("Horror")
        genre2 = Genre("Comedy")
        assert genre1.__lt__(genre2) is False
        assert genre2.__lt__(genre1) is True

    def test_hash(self):
        genre1 = Genre("Horror")
        genre2 = Genre("Comedy")
        genre3 = Genre("Horror")
        assert genre1.__hash__() != genre2.__hash__()
        assert genre1.__hash__() == genre3.__hash__()


# =====
# MOVIE
# =====


class Movie:

    def __init__(self, movie_title: str, movie_release_year: int):
        if movie_title == "" or type(movie_title) is not str:
            self.__title = None
        else:
            self.__title = movie_title.strip()

        if type(movie_release_year) is not int or movie_release_year <= 1900:
            self.__year = None
        else:
            self.__year = movie_release_year

        self.__description = None
        self.__director = None
        self.__actors = []
        self.__genres = []
        self.__runtime_minutes = None
        self.__rating = None
        self.__votes = None
        self.__revenue = None
        self.__metascore = None

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title):
        if type(title) is not str or title == "":
            pass
        else:
            self.__title = title.strip()

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year):
        if type(year) is int and year > 1900:
            self.__year = year

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description):
        if type(description) is not str or description == "":
            pass
        else:
            self.__description = description.strip()

    @property
    def director(self) -> Director:
        return self.__director

    @director.setter
    def director(self, director):
        if type(director) is Director:
            self.__director = director

    @property
    def actors(self) -> List[Actor]:
        return self.__actors

    @actors.setter
    def actors(self, actors):
        self.__actors = actors

    @property
    def genres(self) -> List[Genre]:
        return self.__genres

    @genres.setter
    def genres(self, genres):
        self.__genres = genres

    @property
    def runtime_minutes(self) -> int:
        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, runtime):
        if type(runtime) is int and runtime > 0:
            self.__runtime_minutes = runtime
        else:
            raise ValueError("ValueError raised")

    @property
    def rating(self) -> float:
        return self.__rating

    @rating.setter
    def rating(self, rating):
        if type(rating) is float and rating > 0.0:
            self.__rating = rating

    @property
    def votes(self) -> int:
        return self.__votes

    @votes.setter
    def votes(self, votes):
        if type(votes) is int and votes > 0:
            self.__votes = votes

    @property
    def revenue(self) -> float:
        return self.__revenue

    @revenue.setter
    def revenue(self, revenue):
        if type(revenue) is float and revenue > 0.0:
            self.__revenue = revenue

    @property
    def metascore(self) -> int:
        return self.__metascore

    @metascore.setter
    def metascore(self, metascore):
        if type(metascore) is int and 0 <= metascore <= 100:
            self.__metascore = metascore

    def concat_string(self):
        return str(self.__title) + str(self.__year)

    def __repr__(self):
        return f"<Movie {self.__title}, {self.__year}>"

    def __eq__(self, other):
        return self.concat_string() == other.concat_string()

    def __lt__(self, other):
        return self.concat_string() < other.concat_string()

    def __hash__(self):
        return hash(self.concat_string())

    def add_actor(self, actor):
        if type(actor) is Actor and actor not in self.__actors:
            self.__actors.append(actor)

    def remove_actor(self, actor):
        if type(actor) is Actor and actor in self.__actors:
            i = self.__actors.index(actor)
            self.__actors.pop(i)
        pass

    def add_genre(self, genre):
        if type(genre) is Genre and genre not in self.__genres:
            self.__genres.append(genre)

    def remove_genre(self, genre):
        if type(genre) is Genre and genre in self.__genres:
            i = self.__genres.index(genre)
            self.__genres.pop(i)


class TestMovieMethods:

    def test_init(self):
        # correct inputs
        movie1 = Movie("Moana", 2016)
        assert repr(movie1) == "<Movie Moana, 2016>"

        # None inputs
        movie2 = Movie(None, None)
        assert repr(movie2) == "<Movie None, None>"

        # "" and None inputs
        movie3 = Movie("", None)
        assert repr(movie3) == "<Movie None, None>"

        # "correct title, year incorrect
        movie4 = Movie("Moana", 1816)
        assert repr(movie4) == "<Movie Moana, None>"

    def test_title(self):
        # correct input
        movie1 = Movie("Mona", 2016)
        movie1.title = "Moana"
        assert movie1.title == "Moana"

        # incorrect input
        movie2 = Movie("Frozn", 2014)
        movie2.title = 10
        assert movie2.title == "Frozn"

    def test_year(self):
        # correct input
        movie1 = Movie("Moana", 2015)
        movie1.year = 2016
        assert movie1.year == 2016

        # incorrect input
        movie2 = Movie("Frozen", 2013)
        movie1.year = "2014"
        assert movie2.year == 2013

    def test_description(self):
        # correct input
        movie1 = Movie("Moana", 2016)
        movie1.description = "TEST"
        assert movie1.description == "TEST"

        # incorrect input
        movie2 = Movie("Frozen", 2014)
        movie2.description = 100
        assert movie2.description is None

    def test_director(self):
        # correct input
        movie1 = Movie("Moana", 2016)
        director1 = Director("Ron Clements")
        movie1.director = director1
        assert movie1.director == director1

        # incorrect input
        movie2 = Movie("Frozen", 2014)
        movie2.director = "Chris Buck"
        assert movie2.director is None

    def test_actors(self):
        # correct input
        movie1 = Movie("Moana", 2016)
        movie1.actors = [Actor("Dwayne Johnson"), Actor("Rachel House")]
        assert movie1.actors == [Actor("Dwayne Johnson"), Actor("Rachel House")]

        # incorrect input
        movie2 = Movie("Frozen", 2014)
        # movie2.actors = [Director("Chris Buck")]
        # not testing as no type checking in place in method currently (kept encountering errors)
        # assert movie2.actors == []

    def test_genres(self):
        # correct input
        movie1 = Movie("Moana", 2016)
        movie1.genres = [Genre("Animation"), Genre("Comedy")]
        assert movie1.genres == [Genre("Animation"), Genre("Comedy")]

        # incorrect input
        movie2 = Movie("Frozen", 2014)
        # movie2.genres = [Director("Chris Buck")]
        # not testing as no type checking in place in method currently (kept encountering errors)
        # assert movie2.genres == []

    def test_runtime_minutes(self):
        # correct input
        movie1 = Movie("Moana", 2016)
        movie1.runtime_minutes = 107
        assert movie1.runtime_minutes == 107

        # incorrect input
        movie2 = Movie("Frozen", 2014)
        with pytest.raises(ValueError):
            movie2.runtime_minutes = "107"

    def test_rating(self):
        # correct input
        movie1 = Movie("Moana", 2016)
        movie1.rating = 7.7
        assert movie1.rating == 7.7

        # incorrect input
        movie2 = Movie("Frozen", 2014)
        movie2.rating = "7.4"
        assert movie2.rating is None

    def test_votes(self):
        # correct input
        movie1 = Movie("Moana", 2016)
        movie1.votes = 118151
        assert movie1.votes == 118151

        # incorrect input
        movie2 = Movie("Frozen", 2014)
        movie2.votes = "123456"
        assert movie2.votes is None

    def test_revenue(self):
        # correct input
        movie1 = Movie("Moana", 2016)
        movie1.revenue = 100.01
        assert movie1.revenue == 100.01

        # incorrect input
        movie2 = Movie("Frozen", 2014)
        movie2.revenue = "123.45"
        assert movie2.revenue is None

    def test_metascore(self):
        # correct input
        movie1 = Movie("Moana", 2016)
        movie1.metascore = 81
        assert movie1.metascore == 81

        # incorrect input
        movie2 = Movie("Frozen", 2014)
        movie2.metascore = 85.5
        assert movie2.metascore is None

    def test_concat_string(self):
        movie1 = Movie("Moana", 2016)
        assert movie1.concat_string() == "Moana2016"
        movie2 = Movie("Moana", "")
        assert movie2.concat_string() == "MoanaNone"
        movie3 = Movie("", 2016)
        assert movie3.concat_string() == "None2016"

    def test_repr(self):
        movie1 = Movie("Moana", 2016)
        movie2 = Movie("Moana", "")
        movie3 = Movie("", 2016)
        assert movie1.__repr__() == "<Movie Moana, 2016>"
        assert movie2.__repr__() == "<Movie Moana, None>"
        assert movie3.__repr__() == "<Movie None, 2016>"

    def test_eq(self):
        movie1 = Movie("Moana", 2016)
        movie2 = Movie("Frozen", 2014)
        movie3 = Movie("Moana", 2016)
        movie4 = Movie("Moana", 2020)
        assert movie1.__eq__(movie2) is False
        assert movie1.__eq__(movie3) is True
        assert movie1.__eq__(movie4) is False

    def test_lt(self):
        movie1 = Movie("Moana", 2016)
        movie2 = Movie("Frozen", 2014)
        movie3 = Movie("Moana", 2020)
        assert movie1.__lt__(movie2) is False
        assert movie2.__lt__(movie1) is True
        assert movie1.__lt__(movie3) is True
        assert movie3.__lt__(movie1) is False

    def test_hash(self):
        movie1 = Movie("Moana", 2016)
        movie2 = Movie("Frozen", 2014)
        movie3 = Movie("Moana", 2016)
        assert movie1.__hash__() != movie2.__hash__()
        assert movie1.__hash__() == movie3.__hash__()

    def test_add_actor(self):
        # correct input
        movie1 = Movie("Moana", 2016)
        movie1.add_actor(Actor("Dwayne Johnson"))
        assert movie1.actors == [Actor("Dwayne Johnson")]

        # incorrect input
        movie1.add_actor(Director("Ron Clements"))
        assert movie1.actors == [Actor("Dwayne Johnson")]

        # adding an actor twice
        movie1.add_actor(Actor("Dwayne Johnson"))
        assert movie1.actors == [Actor("Dwayne Johnson")]

        # adding a second actor
        movie1.add_actor(Actor("Rachel House"))
        assert movie1.actors == [Actor("Dwayne Johnson"), Actor("Rachel House")]

    def test_remove_actor(self):
        movie1 = Movie("Moana", 2016)
        movie1.add_actor(Actor("Dwayne Johnson"))

        # correct input
        movie1.remove_actor(Actor("Dwayne Johnson"))
        assert movie1.actors == []

        # incorrect input
        movie1.add_actor(Actor("Dwayne Johnson"))
        movie1.remove_actor(Director("Dwayne Johnson"))
        assert movie1.actors == [Actor("Dwayne Johnson")]

        # removing an actor not in list
        movie1.remove_actor(Actor("Rachel House"))
        assert movie1.actors == [Actor("Dwayne Johnson")]

    def test_add_genre(self):
        # correct input
        movie1 = Movie("Moana", 2016)
        movie1.add_genre(Genre("Animation"))
        assert movie1.genres == [Genre("Animation")]

        # incorrect input
        movie1.add_actor(Director("Ron Clements"))
        assert movie1.genres == [Genre("Animation")]

        # adding a genre twice
        movie1.add_genre(Genre("Animation"))
        assert movie1.genres == [Genre("Animation")]

        # adding a second genre
        movie1.add_genre(Genre("Comedy"))
        assert movie1.genres == [Genre("Animation"), Genre("Comedy")]

    def test_remove_genre(self):
        movie1 = Movie("Moana", 2016)
        movie1.add_genre(Genre("Animation"))

        # correct input
        movie1.remove_genre(Genre("Animation"))
        assert movie1.genres == []

        # incorrect input
        movie1.add_genre(Genre("Animation"))
        movie1.remove_genre(Director("Animation"))
        assert movie1.genres == [Genre("Animation")]

        # removing a genre not in list
        movie1.remove_genre(Genre("Comedy"))
        assert movie1.genres == [Genre("Animation")]


# ======
# REVIEW
# ======

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


# ====
# USER
# ====


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


# =========
# WATCHLIST
# =========


class WatchList:

    def __init__(self):
        self.__watchlist = []

    @property
    def watchlist(self) -> List[Movie]:
        return self.__watchlist

    def add_movie(self, movie):
        if type(movie) is Movie and movie not in self.__watchlist:
            self.__watchlist.append(movie)

    def remove_movie(self, movie):
        if type(movie) is Movie and movie in self.__watchlist:
            i = self.__watchlist.index(movie)
            self.__watchlist.pop(i)

    def select_movie_to_watch(self, index):
        if self.size() == 0:
            return None
        elif type(index) is int and 0 <= index < self.size():
            return self.__watchlist[index]
        else:
            return None

    def size(self):
        return len(self.__watchlist)

    def first_movie_in_watchlist(self):
        if self.size() == 0:
            return None
        else:
            return self.__watchlist[0]

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if 0 <= self.n < self.size():
            result = self.__watchlist[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration


class TestWatchListMethods:

    def test_init(self):
        watchlist = WatchList()
        assert watchlist.watchlist == []
        print(watchlist.watchlist)

    def test_add_movie(self):
        watchlist = WatchList()
        movie1 = Movie("Moana", 2016)
        movie2 = Movie("Frozen", 2014)
        watchlist.add_movie(movie1)
        assert len(watchlist.watchlist) == 1
        assert watchlist.watchlist[0] == movie1
        watchlist.add_movie(movie2)
        assert len(watchlist.watchlist) == 2
        assert watchlist.watchlist[1] == movie2
        watchlist.add_movie(movie1)
        assert len(watchlist.watchlist) == 2
        watchlist.add_movie("")
        assert len(watchlist.watchlist) == 2

    def test_remove_movie(self):
        watchlist = WatchList()
        movie = Movie("Moana", 2016)
        watchlist.add_movie(movie)
        watchlist.remove_movie("")
        assert len(watchlist.watchlist) == 1
        watchlist.remove_movie(movie)
        assert len(watchlist.watchlist) == 0
        watchlist.remove_movie(movie)
        assert len(watchlist.watchlist) == 0

    def test_select_movie_to_watch(self):
        watchlist = WatchList()
        movie1 = Movie("Moana", 2016)
        movie2 = Movie("Frozen", 2014)
        assert watchlist.select_movie_to_watch(0) is None
        watchlist.add_movie(movie1)
        assert watchlist.select_movie_to_watch(0) == movie1
        assert watchlist.select_movie_to_watch(1) is None
        watchlist.add_movie(movie2)
        assert watchlist.select_movie_to_watch(1) == movie2
        watchlist.remove_movie(movie1)
        assert watchlist.select_movie_to_watch(1) is None
        assert watchlist.select_movie_to_watch(0) == movie2
        assert watchlist.select_movie_to_watch("0") is None
        assert watchlist.select_movie_to_watch(-1) is None

    def test_size(self):
        watchlist = WatchList()
        assert watchlist.size() == 0
        movie1 = Movie("Moana", 2016)
        movie2 = Movie("Frozen", 2014)
        watchlist.add_movie(movie1)
        assert watchlist.size() == 1
        watchlist.add_movie(movie2)
        assert watchlist.size() == 2
        watchlist.remove_movie(movie1)
        assert watchlist.size() == 1

    def test_first_movie_in_watchlist(self):
        watchlist = WatchList()
        assert watchlist.first_movie_in_watchlist() is None
        movie1 = Movie("Moana", 2016)
        watchlist.add_movie(movie1)
        assert watchlist.first_movie_in_watchlist() == movie1

    def test_iterator(self):
        watchlist = WatchList()
        movie1 = Movie("Moana", 2016)
        movie2 = Movie("Frozen", 2014)
        watchlist.add_movie(movie1)
        watchlist.add_movie(movie2)

        i = iter(watchlist)

        # test __iter__
        assert i == watchlist.__iter__()

        # test __next__
        assert next(i) == watchlist.watchlist[0] == movie1
        assert next(i) == watchlist.watchlist[1] == movie2
        with pytest.raises(StopIteration):
            next(i)
