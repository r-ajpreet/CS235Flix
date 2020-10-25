import abc
from typing import List
from datetime import date

from flix.domain.model import Actor, Director, Genre, Movie, Review, User, WatchList


class RepositoryException(Exception):

    def __init__(self, message=None):
        pass


class AbstractRepository(abc.ABC):

    ###################
    # User management #
    ###################

    @abc.abstractmethod
    def add_user(self, user: User):
        """ Adds a User to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self, username) -> User:
        """ Returns the User named username from the repository.

        If there is no User with the given username, this method returns None.
        """
        raise NotImplementedError

    ####################
    # Movie management #
    ####################

    @abc.abstractmethod
    def add_movie(self, movie: Movie):
        """ Adds a Movie to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie(self, rank: int) -> Movie:
        """ Returns Movie with rank (id) from the repository.

        If there is no Movie with the given rank, this method returns None.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_number_of_movies(self):
        """ Returns the number of Movies in the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_by_year(self, target_year: int) -> List[Movie]:
        """ Returns a list of Movies from the given year

        If there are no matches, this method returns an empty list.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_first_movie(self) -> Movie:
        """ Returns the first Movie, ordered by year, from the repository.

        Returns None if the repository is empty.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_last_movie(self) -> Movie:
        """ Returns the last Movie, ordered by year, from the repository.

        Returns None if the repository is empty.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_by_rank(self, rank_list):
        """ Returns a list of Movies, whose ranks match those in rank_list, from the repository.

        If there are no matches, this method returns an empty list.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_year_of_previous_movie(self, movie: Movie):
        """ Returns the year of a Movie that immediately precedes movie.

         If movie is the first Movie in the repository, this methods returns None
         because there are no Movies from a previous year.
         """
        raise NotImplementedError

    @abc.abstractmethod
    def get_year_of_next_movie(self, movie: Movie):
        """ Returns the year of a Movie that immediately follows movie.

        If movie is the last Movie in the repository, this method returns None
        because there are no Movies from a later year.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_by_title(self, title: str) -> List[Movie]:
        """ Returns a list of Movies where the title contains the given string. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_by_actor(self, actor: Actor) -> List[Movie]:
        """ Returns a list of Movies that feature the given Actor. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_by_director(self, director: Director) -> List[Movie]:
        """ Returns a list of Movies directed by the given Director. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_by_genre(self, genre: Genre) -> List[Movie]:
        """ Returns a list of Movies that are of the given Genre. """
        raise NotImplementedError

    ##############################
    # Movie attribute management #
    ##############################

    @abc.abstractmethod
    def add_actor(self, actor: Actor):
        """ Adds an Actor to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_actors(self) -> List[Actor]:
        """ Returns the Actors stored in the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def add_director(self, director: Director):
        """ Adds a Director to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_directors(self) -> List[Director]:
        """ Returns the Directors in the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def add_genre(self, genre: Genre):
        """ Adds a Genre to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_genres(self) -> List[Genre]:
        """ Returns the Genres in the repository. """
        raise NotImplementedError

    #####################
    # Review management #
    #####################

    @abc.abstractmethod
    def add_review(self, review: Review):
        """ Adds a Review to the repository.

        If the Review doesn't have bidirectional links with a Movie and a User,
        this method raises a RepositoryException and doesn't update the repository.
        """
        if review.user is None or review not in review.user.reviews:
            raise RepositoryException('Review not correctly attached to a User')
        if review.movie is None or review not in review.movie.reviews:
            raise RepositoryException('Review not correctly attached to a Movie')

    @abc.abstractmethod
    def get_reviews(self) -> List[Review]:
        """ Returns the Reviews stored in the repository. """
        raise NotImplementedError
