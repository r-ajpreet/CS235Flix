"""
Domain Model, contains classes for:
Actor; Director; Genre; Movie; Review; User; WatchList
"""

from datetime import datetime
from typing import List

import pytest


# =====
# ACTOR
# =====

class Actor:

    def __init__(self, actor_full_name: str):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name.strip()
        self.__colleagues = list()

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

        self.__rank = None
        self.__description = None
        self.__director = None
        self.__actors = []
        self.__genres = []
        self.__runtime_minutes = None
        self.__rating = None
        self.__votes = None
        self.__revenue = None
        self.__metascore = None
        self.__reviews: List[Review] = list()

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
    def rank(self) -> int:
        return self.__rank

    @rank.setter
    def rank(self, rank):
        if type(rank) is int and rank >= 0:
            self.__rank = rank

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

    @property
    def reviews(self):
        return self.__reviews

    @reviews.setter
    def reviews(self, reviews):
        if type(reviews) == List[Review]:
            self.__reviews = reviews

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
    def reviews(self):
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


# ======
# REVIEW
# ======

class Review:

    def __init__(self, user: User, movie: Movie, review_text: str, rating: int, timestamp: datetime):
        if type(user) is User:
            self.__user = user
        else:
            self.__user = None

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

        if type(timestamp) is datetime:
            self.__timestamp = datetime
        else:
            self.__timestamp = None

    @property
    def user(self) -> User:
        return self.__user

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
        username = self.user.user_name
        return f"User: {username}\nReview: {self.__review_text}\nRating: {self.__rating}"

    def __eq__(self, other):
        return (self.__user == other.__user and
                self.__movie == other.__movie and
                self.__review_text == other.__review_text and
                self.__rating == other.__rating and
                self.__timestamp == other.__timestamp)


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


###########################
# Other classes/functions #
###########################

class ModelException(Exception):
    pass


def make_review(user: User, movie: Movie, review_text: str, rating: int, timestamp: datetime = datetime.now()):
    review = Review(user, movie, review_text, rating, timestamp)
    user.add_review(review)
    movie.add_review(review)

    return review


def make_tag_association(movie: Movie, tag):
    # TODO
    pass
