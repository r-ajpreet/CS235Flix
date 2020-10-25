from datetime import date, datetime
from typing import List
import os

import pytest

from flix.domain.model import Actor, Director, Genre, Movie, Review, User, WatchList, make_review
from flix.adapters import memory_repository, repository
from flix.adapters.memory_repository import MemoryRepository
from flix.adapters.repository import RepositoryException


TEST_DATA_PATH = os.path.join(
    "/Users/rajpreetsingh/Dropbox/Raj/UoA/2020/2 - Semester Two/COMPSCI 235/Assessments/CS235Flix/tests/data")


@pytest.fixture
def in_memory_repo():
    repo = MemoryRepository()
    memory_repository.populate(TEST_DATA_PATH, repo)
    return repo
    pass


###################
# User management #
###################

def test_repository_add_user(in_memory_repo):
    user = User('rsin774', 'password')
    in_memory_repo.add_user(user)

    assert in_memory_repo.get_user('rsin774') is User


def test_repository_get_user(in_memory_repo):
    # Existing user
    user = in_memory_repo.get_user('rsin774')
    assert user == User('rsin774', 'password')

    # Non-existent user
    user = in_memory_repo.get_user('doesntexist')
    assert user is None


####################
# Movie management #
####################

def test_repository_add_movie(in_memory_repo):
    movie = Movie("Guardians of the Galaxy", 2014)
    in_memory_repo.add_movie(movie)

    assert in_memory_repo.get_movie(0) is movie


def test_repository_get_movie(in_memory_repo):
    movie = in_memory_repo.get_movie(0)

    # Check that the Article has the expected title.
    assert movie.title == "Guardians of the Galaxy"

    # Check that the Movie is reviewed as expected.
    # review_one = [review for review in movie.reviews if review.review_text == 'Liked it.'][0]
    # assert review_one.user.user_name == 'rsin774'

    # Check that the Movie is tagged as expected.
    # assert movie.is_tagged_by(Tag('Action'))


def test_repository_get_movie_non_existent(in_memory_repo):
    movie = in_memory_repo.get_movie(1000)
    assert movie is None


def test_repository_get_number_of_movies(in_memory_repo):
    number_of_movies = in_memory_repo.get_number_of_movies()

    # Check that the query returned 1000 movies.
    assert number_of_movies == 1000


def test_repository_get_movies_by_year(in_memory_repo):
    movies = in_memory_repo.get_movies_by_year(2016)

    # Check that the query returned 297 movies.
    assert len(movies) == 297


def test_repository_get_movies_by_year_none_in_year(in_memory_repo):
    movies = in_memory_repo.get_movies_by_year(2025)
    assert len(movies) == 0


def test_repository_get_first_movie(in_memory_repo):
    movie = in_memory_repo.get_first_movie()
    assert movie.title == "Guardians of the Galaxy"


def test_repository_get_last_movie(in_memory_repo):
    movie = in_memory_repo.get_last_movie()
    assert movie.title == "Nine Lives"


def test_repository_get_movies_by_rank(in_memory_repo):
    movies = in_memory_repo.get_movies_by_rank([0, 2, 4])

    assert len(movies) == 3
    assert movies[0].title == "Guardians of the Galaxy"
    assert movies[1].title == "Prometheus"
    assert movies[2].title == "Split"


def test_repository_get_movies_by_rank_for_non_existent_rank(in_memory_repo):
    movies = in_memory_repo.get_movies_by_rank([999, 1000])

    assert len(movies) == 1
    assert movies[0].title == "Nine Lives"


def test_repository_get_movies_by_rank_non_existent_ranks(in_memory_repo):
    movies = in_memory_repo.get_movies_by_rank([1000, 1001])

    assert len(movies) == 0


def test_repository_get_year_of_previous_movie(in_memory_repo):
    movie = in_memory_repo.get_movie(1)
    previous_year = in_memory_repo.get_year_of_previous_movie(movie)

    assert previous_year == '2014'


def test_repository_get_year_of_previous_movie_when_no_previous(in_memory_repo):
    movie = in_memory_repo(0)
    previous_year = in_memory_repo.get_year_of_previous_movie(movie)

    assert previous_year is None


def test_repository_get_year_of_next_movie(in_memory_repo):
    movie = in_memory_repo.get_movie(1)
    next_year = in_memory_repo.get_year_of_next_movie(movie)

    assert next_year == '2016'


def test_repository_get_year_of_next_movie_when_no_next(in_memory_repo):
    movie = in_memory_repo.get_movie(999)
    next_year = in_memory_repo.get_year_of_next_movie(movie)

    assert next_year is None


def test_repository_get_movies_by_title(in_memory_repo):
    # TODO
    pass


def test_repository_get_movies_by_title_non_existent(in_memory_repo):
    movies = in_memory_repo.get_movies_by_title("DDLJ")
    assert len(movies) == 0


def test_repository_get_movies_by_actor(in_memory_repo):
    # TODO
    pass


def test_repository_get_movies_by_actor_non_existent(in_memory_repo):
    movies = in_memory_repo.get_movies_by_actor("SRK")
    assert len(movies) == 0


def test_repository_get_movies_by_director(in_memory_repo):
    # TODO
    pass


def test_repository_get_movies_by_director_non_existent(in_memory_repo):
    movies = in_memory_repo.get_movies_by_director("MNS")
    assert len(movies) == 0


def test_repository_get_movies_by_genre(in_memory_repo):
    # TODO
    pass


def test_repository_get_movies_by_genre_non_existent(in_memory_repo):
    movies = in_memory_repo.get_movies_by_genre("AAA")
    assert len(movies) == 0


##############################
# Movie attribute management #
##############################

def test_repository_add_actor(in_memory_repo):
    actor = Actor("Shah Rukh Khan")
    in_memory_repo.add_actor(actor)

    assert actor in in_memory_repo.get_actors()


def test_repository_get_actors(in_memory_repo):
    actors = in_memory_repo.get_actors()

    assert len(actors) == 100  # CHANGE TO CORRECT AMT


def test_repository_add_director(in_memory_repo):
    director = Director("Cames Jameron")
    in_memory_repo.add_director(director)

    assert director in in_memory_repo.get_directors()


def test_repository_get_directors(in_memory_repo):
    directors = in_memory_repo.get_directors()

    assert len(directors) == 25  # CHANGE TO CORRECT AMT


def test_repository_add_genre(in_memory_repo):
    genre = Genre("MEGAFUN")
    in_memory_repo.add_genre(genre)

    assert genre in in_memory_repo.get_genre()


def test_repository_get_genres(in_memory_repo):
    genres = in_memory_repo.get_genres()

    assert len(genres) == 30  # CHANGE TO CORRECT AMT


#####################
# Review management #
#####################

def test_repository_add_review(in_memory_repo):
    user = User('rsin774', 'password')
    movie = Movie('Guardians of the Galaxy', 2014)
    review = make_review(user, movie, "Great!", 10, datetime.now())

    in_memory_repo.add_review(review)

    assert review in in_memory_repo.get_reviews()


def test_repository_add_review_without_user(in_memory_repo):
    movie = Movie('Guardians of the Galaxy', 2014)
    review = make_review(None, movie, "Great!", 10, datetime.now())

    with pytest.raises(RepositoryException):
        in_memory_repo.add_review(review)


def test_repository_add_review_without_movie(in_memory_repo):
    user = in_memory_repo.get_user('rsin774')
    movie = in_memory_repo.get_movie(1)
    review = Review(None, movie, "Great!", 10, datetime.now())

    user.add_review(review)

    with pytest.raises(RepositoryException):
        # Exception expected because the Movie doesn't refer to the Review.
        in_memory_repo.add_review(review)


def test_repository_get_reviews(in_memory_repo):
    reviews = in_memory_repo.get_reviews()

    assert len(reviews) == 5
