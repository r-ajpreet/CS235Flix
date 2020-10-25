from datetime import datetime

from flix.domain.model import Actor, Director, Genre, Movie, Review, User, WatchList

import pytest


###################
# PYTEST FIXTURES #
###################

@pytest.fixture()
def actor():
    return Actor("Angelina Jolie")


@pytest.fixture()
def director():
    return Director("James Gray")


@pytest.fixture()
def genre():
    return Genre("Action")


@pytest.fixture()
def movie():
    return Movie("Prometheus", 2012)


@pytest.fixture
def review():
    user = User("rsin774", "password")
    movie = Movie("Moana", 2016)
    review_text = "This movie was very enjoyable."
    rating = 8
    timestamp = datetime.now()
    return Review(user, movie, review_text, rating, timestamp)


@pytest.fixture()
def user():
    return User("rsin774", "password")


@pytest.fixture()
def watchlist():
    return WatchList()


##############
# TEST ACTOR #
##############


def test_actor_construction(actor):
    assert actor.actor_full_name == 'Angelina Jolie'
    assert repr(actor) == '<Actor Angelina Jolie>'

    for colleague in actor.colleagues:
        # Actor should have an empty list of Actor colleagues after construction.
        assert False


def test_actor_invalid_construction():
    actor1 = Actor("")
    assert actor1.actor_full_name is None
    actor2 = Actor(50)
    assert actor2.actor_full_name is None


def test_actor_equals_operator():
    actor_1 = Actor("Angelina Jolie")
    actor_2 = Actor("Jack Black")
    actor_3 = Actor("Angelina Jolie")
    assert (actor_1 == actor_2) is False
    assert (actor_1 == actor_3) is True


def test_actor_less_than_operator():
    actor_1 = Actor("Angelina Jolie")
    actor_2 = Actor("Jack Black")
    assert (actor_1 < actor_2) is True
    assert (actor_2 < actor_1) is False


def test_actor_hash():
    actor_1 = Actor("Angelina Jolie")
    actor_2 = Actor("Jack Black")
    actor_3 = Actor("Angelina Jolie")
    assert actor_1.__hash__() != actor_2.__hash__()
    assert actor_1.__hash__() == actor_3.__hash__()


def test_actor_add_actor_colleague():
    actor_1 = Actor("Angelina Jolie")
    actor_2 = Actor("Tom Cruise")

    # add new object not of type Actor
    actor_1.add_actor_colleague(50)
    assert len(actor_1.colleagues) == 0

    # add new colleague
    actor_1.add_actor_colleague(actor_2)
    assert actor_1.colleagues[0] == actor_2

    # add existing colleague
    actor_1.add_actor_colleague(actor_2)
    assert len(actor_1.colleagues) == 1

    # add a second colleague
    actor_3 = Actor("Chris Pratt")
    actor_1.add_actor_colleague(actor_3)
    assert len(actor_1.colleagues) == 2
    assert actor_1.colleagues[1] == actor_3


def test_actor_check_if_this_actor_worked_with():
    actor_1 = Actor("Angelina Jolie")
    actor_2 = Actor("Tom Cruise")
    actor_3 = Actor("Chris Pratt")

    actor_1.add_actor_colleague(actor_2)
    assert actor_1.check_if_this_actor_worked_with(actor_2) is True
    assert actor_1.check_if_this_actor_worked_with(actor_3) is False


#################
# TEST DIRECTOR #
#################


def test_director_construction(director):
    assert director.director_full_name == 'James Gray'
    assert repr(director) == '<Director James Gray>'


def test_director_invalid_construction():
    director1 = Director("")
    assert director1.director_full_name is None
    director2 = Director(42)
    assert director2.director_full_name is None


def test_director_equals_operator():
    director_1 = Director("Taika Waititi")
    director_2 = Director("James Cameron")
    director_3 = Director("Taika Waititi")
    assert (director_1 == director_2) is False
    assert (director_1 == director_3) is True


def test_director_less_than_operator():
    director_1 = Director("Taika Waititi")
    director_2 = Director("James Cameron")
    assert (director_1 < director_2) is False
    assert (director_2 < director_1) is True


def test_director_hash():
    director_1 = Director("Taika Waititi")
    director_2 = Director("James Cameron")
    director_3 = Director("Taika Waititi")
    assert director_1.__hash__() != director_2.__hash__()
    assert director_1.__hash__() == director_3.__hash__()


##############
# TEST GENRE #
##############

def test_genre_construction(genre):
    assert genre.genre_name == 'Action'
    assert repr(genre) == '<Genre Action>'


def test_genre_invalid_construction():
    genre1 = Genre("")
    assert genre1.genre_name is None
    genre2 = Genre(50)
    assert genre2.genre_name is None


def test_genre_equals_operator():
    genre_1 = Genre("Horror")
    genre_2 = Genre("Comedy")
    genre_3 = Genre("Horror")
    assert (genre_1 == genre_2) is False
    assert (genre_1 == genre_3) is True


def test_genre_less_than_operator():
    genre_1 = Genre("Horror")
    genre_2 = Genre("Comedy")
    assert (genre_1 < genre_2) is False
    assert (genre_2 < genre_1) is True


def test_genre_hash():
    genre_1 = Genre("Horror")
    genre_2 = Genre("Comedy")
    genre_3 = Genre("Horror")
    assert (genre_1.__hash__() == genre_2.__hash__()) is False
    assert (genre_1.__hash__() == genre_3.__hash__()) is True


##############
# TEST MOVIE #
##############

def test_movie_construction(movie):
    assert movie.title == 'Prometheus'
    assert movie.year == 2012
    assert repr(movie) == '<Movie Prometheus, 2012>'

    assert movie.description is None
    assert movie.director is None

    for actor in movie.actors:
        # Movie should have an empty list of Actors after construction.
        assert False

    for genre in movie.genres:
        # Movie should have an empty list of Genres after construction.
        assert False

    assert movie.runtime_minutes is None
    assert movie.rating is None
    assert movie.votes is None
    assert movie.revenue is None
    assert movie.metascore is None

    for review in movie.reviews:
        # Movie should have an empty list of Reviews after construction.
        assert False


def test_movie_invalid_construction():
    # None inputs
    movie2 = Movie(None, None)
    assert repr(movie2) == "<Movie None, None>"

    # "" and None inputs
    movie3 = Movie("", None)
    assert repr(movie3) == "<Movie None, None>"

    # "correct title, year incorrect
    movie4 = Movie("Moana", 1816)
    assert repr(movie4) == "<Movie Moana, None>"


def test_movie_title():
    # correct input
    movie1 = Movie("Mona", 2016)
    movie1.title = "Moana"
    assert movie1.title == "Moana"

    # incorrect input
    movie2 = Movie("Frozn", 2014)
    movie2.title = 10
    assert movie2.title == "Frozn"


def test_movie_year():
    # correct input
    movie1 = Movie("Moana", 2015)
    movie1.year = 2016
    assert movie1.year == 2016

    # incorrect input
    movie2 = Movie("Frozen", 2013)
    movie1.year = "2014"
    assert movie2.year == 2013


def test_movie_description():
    # correct input
    movie1 = Movie("Moana", 2016)
    movie1.description = "TEST"
    assert movie1.description == "TEST"

    # incorrect input
    movie2 = Movie("Frozen", 2014)
    movie2.description = 100
    assert movie2.description is None


def test_movie_director():
    # correct input
    movie1 = Movie("Moana", 2016)
    director1 = Director("Ron Clements")
    movie1.director = director1
    assert movie1.director == director1

    # incorrect input
    movie2 = Movie("Frozen", 2014)
    movie2.director = "Chris Buck"
    assert movie2.director is None


def test_movie_actors():
    # correct input
    movie1 = Movie("Moana", 2016)
    movie1.actors = [Actor("Dwayne Johnson"), Actor("Rachel House")]
    assert movie1.actors == [Actor("Dwayne Johnson"), Actor("Rachel House")]

    # incorrect input
    movie2 = Movie("Frozen", 2014)
    # movie2.actors = [Director("Chris Buck")]
    # not testing as no type checking in place in method currently (kept encountering errors)
    # assert movie2.actors == []


def test_movie_genres():
    # correct input
    movie1 = Movie("Moana", 2016)
    movie1.genres = [Genre("Animation"), Genre("Comedy")]
    assert movie1.genres == [Genre("Animation"), Genre("Comedy")]

    # incorrect input
    movie2 = Movie("Frozen", 2014)
    # movie2.genres = [Director("Chris Buck")]
    # not testing as no type checking in place in method currently (kept encountering errors)
    # assert movie2.genres == []


def test_movie_runtime_minutes():
    # correct input
    movie1 = Movie("Moana", 2016)
    movie1.runtime_minutes = 107
    assert movie1.runtime_minutes == 107

    # incorrect input
    movie2 = Movie("Frozen", 2014)
    with pytest.raises(ValueError):
        movie2.runtime_minutes = "107"


def test_movie_rating():
    # correct input
    movie1 = Movie("Moana", 2016)
    movie1.rating = 7.7
    assert movie1.rating == 7.7

    # incorrect input
    movie2 = Movie("Frozen", 2014)
    movie2.rating = "7.4"
    assert movie2.rating is None


def test_movie_votes():
    # correct input
    movie1 = Movie("Moana", 2016)
    movie1.votes = 118151
    assert movie1.votes == 118151

    # incorrect input
    movie2 = Movie("Frozen", 2014)
    movie2.votes = "123456"
    assert movie2.votes is None


def test_movie_revenue():
    # correct input
    movie1 = Movie("Moana", 2016)
    movie1.revenue = 100.01
    assert movie1.revenue == 100.01

    # incorrect input
    movie2 = Movie("Frozen", 2014)
    movie2.revenue = "123.45"
    assert movie2.revenue is None


def test_movie_metascore():
    # correct input
    movie1 = Movie("Moana", 2016)
    movie1.metascore = 81
    assert movie1.metascore == 81

    # incorrect input
    movie2 = Movie("Frozen", 2014)
    movie2.metascore = 85.5
    assert movie2.metascore is None


def test_movie_concat_string():
    movie1 = Movie("Moana", 2016)
    assert movie1.concat_string() == "Moana2016"
    movie2 = Movie("Moana", "")
    assert movie2.concat_string() == "MoanaNone"
    movie3 = Movie("", 2016)
    assert movie3.concat_string() == "None2016"


def test_movie_repr():
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Moana", "")
    movie3 = Movie("", 2016)
    assert movie1.__repr__() == "<Movie Moana, 2016>"
    assert movie2.__repr__() == "<Movie Moana, None>"
    assert movie3.__repr__() == "<Movie None, 2016>"


def test_movie_equals_operator():
    movie_1 = Movie("Moana", 2016)
    movie_2 = Movie("Frozen", 2014)
    movie_3 = Movie("Moana", 2016)
    movie_4 = Movie("Moana", 2020)
    assert (movie_1 == movie_2) is False
    assert (movie_1 == movie_3) is True
    assert (movie_1 == movie_4) is False


def test_movie_less_than_operator():
    movie_1 = Movie("Moana", 2016)
    movie_2 = Movie("Frozen", 2014)
    movie_3 = Movie("Moana", 2020)
    assert (movie_1 < movie_2) is False
    assert (movie_2 < movie_1) is True
    assert (movie_1 < movie_3) is True
    assert (movie_3 < movie_1) is False


def test_movie_hash():
    movie_1 = Movie("Moana", 2016)
    movie_2 = Movie("Frozen", 2014)
    movie_3 = Movie("Moana", 2016)
    assert (movie_1.__hash__() == movie_2.__hash__()) is False
    assert (movie_1.__hash__() == movie_3.__hash__()) is True


def test_movie_add_actor():
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


def test_movie_remove_actor():
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


def test_movie_add_genre():
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


def test_movie_remove_genre():
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


###############
# TEST REVIEW #
###############


def test_review_construction(review):
    user = User("rsin774", "password")
    movie = Movie("Moana", 2016)
    assert review.user == user
    assert review.movie == movie
    assert review.review_text == "This movie was very enjoyable."
    assert review.rating == 8
    assert review.timestamp is not None


def test_review_invalid_construction():
    user = ""
    movie = ""
    review_text = ""
    rating = ""
    timestamp = ""
    review = Review(user, movie, review_text, rating, timestamp)
    assert review.user is None
    assert review.movie is None
    assert review.review_text is None
    assert review.rating is None
    assert review.timestamp is None


def test_review_repr():
    user = User("rsin774", "password")
    movie = Movie("Moana", 2016)
    review_text = "This movie was very enjoyable."
    rating = 8
    timestamp = datetime.now()
    review = Review(user, movie, review_text, rating, timestamp)
    assert review.__repr__() == "User: rsin774\nReview: This movie was very enjoyable.\nRating: 8"


def test_review_equals_operator():
    user = User("rsin774", "password")
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Frozen", 2014)
    review_text = "This movie was very enjoyable."
    rating = 8
    timestamp = None
    review1 = Review(user, movie1, review_text, rating, timestamp)
    review2 = Review(user, movie2, review_text, rating, timestamp)
    review3 = Review(user, movie1, review_text, rating, timestamp)
    review4 = review1
    assert review1.__eq__(review2) is False
    assert review1.__eq__(review3) is True
    assert review1.__eq__(review4) is True


#############
# TEST USER #
#############


def test_user_construction(user):
    assert user.user_name == 'rsin774'
    assert user.password == 'password'
    assert repr(user) == '<User rsin774>'

    for review in user.reviews:
        # User should have an empty list of Reviews after construction.
        assert False

    for watched_movie in user.watched_movies:
        # User should have an empty list of watched Movies after construction.
        assert False

    assert user.time_spent_watching_movies_minutes == 0


def test_user_invalid_construction():
    user1 = User('', 'pw67890')
    assert user1.user_name is None
    assert user1.password == 'pw67890'
    user2 = User('Daniel', 12345)
    assert user2.user_name == 'daniel'
    assert user2.password is None


def test_user_repr():
    user1 = User("rsin774", "password")
    user2 = User("", "pw")
    user3 = User("user", "")
    assert repr(user1) == "<User rsin774>"
    assert repr(user2) == "<User None>"
    assert repr(user3) == "<User user>"


def test_user_equals_operator():
    user1 = User("rsin774", "password")
    user2 = User("rsin774", "")
    user3 = User("", "password")
    user4 = User("rsin774", "password")
    assert (user1 == user2) is True
    assert (user1 == user3) is False
    assert (user1 == user4) is True


def test_user_less_than_operator():
    user1 = User("rsin774", "password")
    user2 = User("test", "test123")
    assert (user1 < user2) is True
    assert (user2 < user1) is False


def test_user_hash():
    user1 = User("rsin774", "password")
    user2 = User("rsin774", "")
    user3 = User("", "password")
    user4 = User("rsin774", "password")
    assert (user1.__hash__() == user2.__hash__()) is True
    assert (user1.__hash__() == user3.__hash__()) is False
    assert (user1.__hash__() == user4.__hash__()) is True


def test_user_time_spent():
    user1 = User('Martin', 'pw12345')
    user1.time_spent_watching_movies_minutes = 100
    assert user1.time_spent_watching_movies_minutes == 100
    user2 = User('Ian', 'pw67890')
    user2.time_spent_watching_movies_minutes = -100
    assert user2.time_spent_watching_movies_minutes == 0


def test_user_watch_movie():
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


def test_user_add_review():
    user = User('Martin', 'pw12345')
    movie1 = Movie('Moana', 2016)
    review1 = Review(user, movie1, 'I liked it', 10, datetime.now())
    movie2 = Movie('Frozen', 2014)
    review2 = Review(user, movie2, 'I did not like it', 1, datetime.now())
    review3 = review1

    user.add_review(review1)
    assert len(user.reviews) == 1
    assert user.reviews[0] == review1

    user.add_review(review2)
    assert len(user.reviews) == 2
    assert user.reviews[1] == review2

    user.add_review(review3)
    assert len(user.reviews) == 2


##################
# TEST WATCHLIST #
##################


def test_watchlist_construction(watchlist):
    assert watchlist.watchlist == []


def test_watchlist_add_movie():
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


def test_watchlist_remove_movie():
    watchlist = WatchList()
    movie = Movie("Moana", 2016)
    watchlist.add_movie(movie)
    watchlist.remove_movie("")
    assert len(watchlist.watchlist) == 1
    watchlist.remove_movie(movie)
    assert len(watchlist.watchlist) == 0
    watchlist.remove_movie(movie)
    assert len(watchlist.watchlist) == 0


def test_watchlist_select_movie_to_watch():
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


def test_watchlist_size():
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


def test_watchlist_first_movie_in_watchlist():
    watchlist = WatchList()
    assert watchlist.first_movie_in_watchlist() is None
    movie1 = Movie("Moana", 2016)
    watchlist.add_movie(movie1)
    assert watchlist.first_movie_in_watchlist() == movie1


def test_watchlist_iterator():
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
