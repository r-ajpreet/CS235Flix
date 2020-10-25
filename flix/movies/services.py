from typing import List, Iterable

from flix.adapters.repository import AbstractRepository
from flix.domain.model import Actor, Director, Genre, Movie, Review, User, WatchList


class NonExistentMovieException(Exception):
    pass


class UnknownUserException(Exception):
    pass


# TODO