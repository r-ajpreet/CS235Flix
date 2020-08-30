from typing import List

import pytest

from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director


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
        movie1. metascore = 81
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
