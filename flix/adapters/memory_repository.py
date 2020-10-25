import csv
import os
from datetime import date, datetime
from typing import List

from bisect import bisect, bisect_left, insort_left

from werkzeug.security import generate_password_hash

from flix.adapters.repository import AbstractRepository, RepositoryException
from flix.domain.model import Actor, Director, Genre, Movie, Review, User, make_review, make_tag_association


class MemoryRepository(AbstractRepository):
    # Movies ordered by year, not rank. rank is assumed unique.

    def __init__(self):
        self._movies = list()
        self._movies_index = dict()
        self._actors = list()
        self._directors = list()
        self._genres = list()
        self._users = list()
        self._reviews = list()

    ###################
    # User management #
    ###################

    def add_user(self, user: User):
        self._users.append(user)

    def get_user(self, username) -> User:
        return next((user for user in self._users if user.username == username), None)

    ####################
    # Movie management #
    ####################

    def add_movie(self, movie: Movie):
        insort_left(self._movies, movie)
        self._movies_index[movie.rank] = movie

    def get_movie(self, rank: id) -> Movie:
        movie = None

        try:
            movie = self._movies_index[rank]
        except KeyError:
            pass  # Ignore exception and return None.

        return movie

    def get_number_of_movies(self):
        return len(self._movies)

    def get_movies_by_year(self, target_year: int) -> List[Movie]:
        target_movie = Movie(
            movie_title=None,
            movie_release_year=target_year
        )
        matching_movies = list()

        try:
            index = self.movie_index(target_movie)
            for movie in self._movies[index:None]:
                if movie.year == target_year:
                    matching_movies.append(movie)
                else:
                    break
        except ValueError:
            # No movies for specified year. Simply returns an empty list.
            pass

        return matching_movies

    def get_first_movie(self) -> Movie:
        movie = None

        if len(self._movies) > 0:
            movie = self._movies[0]
        return movie

    def get_last_movie(self) -> Movie:
        movie = None

        if len(self._movies) > 0:
            movie = self._movies[-1]
        return movie

    def get_movies_by_rank(self, rank_list):
        # Strip out any ranks in rank_list that don't represent Movie ranks in the repository.
        existing_ranks = [rank for rank in rank_list if rank in self._movies_index]

        # Fetch the Movies.
        movies = [self._movies_index[rank] for rank in existing_ranks]
        return movies

    def get_year_of_previous_movie(self, movie: Movie):
        previous_year = None

        try:
            index = self.movie_index(movie)
            for stored_movie in reversed(self._movies[0:index]):
                if stored_movie.year < movie.year:
                    previous_year = stored_movie.year
                    break
        except ValueError:
            # No earlier movies, so return None.
            pass

        return previous_year

    def get_year_of_next_movie(self, movie: Movie):
        next_year = None

        try:
            index = self.movie_index(movie)
            for stored_movie in reversed(self.__movies[0:index]):
                if stored_movie.year > movie.year:
                    next_year = stored_movie.year
                    break
        except ValueError:
            # No subsequent movies, so return None.
            pass

        return next_year

    def get_movies_by_title(self, title: str) -> List[Movie]:
        # TODO
        return []

    def get_movies_by_actor(self, actor: Actor) -> List[Movie]:
        # TODO
        return []

    def get_movies_by_director(self, director: Director) -> List[Movie]:
        # TODO
        return []

    def get_movies_by_genre(self, genre: Genre) -> List[Movie]:
        # TODO
        return []

    ##############################
    # Movie attribute management #
    ##############################

    def add_actor(self, actor: Actor):
        self._actors.append(actor)

    def get_actors(self) -> List[Actor]:
        print('In memory repo, getting Actors')
        return self._actors

    def add_director(self, director: Director):
        self._directors.append(director)

    def get_directors(self) -> List[Director]:
        print('In memory repo, getting Directors')
        return self._directors

    def add_genre(self, genre: Genre):
        self._genres.append(genre)

    def get_genres(self) -> List[Genre]:
        print('In memory repo, getting Genres')
        return self._genres

    #####################
    # Review management #
    #####################

    def add_review(self, review: Review):
        super().add_review(review)
        self._reviews.append(review)

    def get_reviews(self) -> List[Review]:
        return self._reviews

    # Helper method to return movie index.
    def movie_index(self, movie: Movie):
        index = bisect_left(self._movies, movie)
        if index != len(self._movies) and self._movies[index].year == movie.date:
            return index
        raise ValueError


###############################
# READING/PROCESSING CSV FILE #
###############################

def read_csv_file(filename: str):
    with open(filename, mode='r', encoding='utf-8-sig') as infile:
        reader = csv.reader(infile)

        # Read first line of the CSV file.
        headers = next(reader)

        # Read remaining rows from the CSV file.
        for row in reader:
            # Strip any leading/trailing white space from data read.
            row = [item.strip() for item in row]
            yield row


def load_movies_actors_directors_genres(data_path: str, repo: MemoryRepository):
    actors = dict()
    directors = dict()
    genres = dict()

    for data_row in read_csv_file(os.path.join(data_path, 'movies.csv')):

        movie_rank = int(data_row[0])
        number_of_tags = len(data_row) - 0  # CHANGE TO CORRECT NUMBER
        movie_tags = data_row[-number_of_tags:]

        # Add any new tags; associate the current movie with tags.
        # for tag in movie_tags:
        #     if tag not in tags.keys():
        #         tags[tag] = list()
        #     tags[tag].append(movie_rank)

        #     del data_row[-number_of_tags:]

            # Create Movie object.
            # movie = Movie(
                # TODO
            # )

            # Add the Movie to the repository.
            # repo.add_movie(movie)

        # Create Tag objects, associate them with Articles and add them to the repository.
        # for tag_name in tags.keys():
        #     tag = Tag(tag_name)
        #     for movie_rank in tags[tag_name]:
        #         article = repo.get_movie(movie_rank)
        #         make_tag_association(movie, tag)
        #     repo.add_tag(tag)


def load_users(data_path: str, repo: MemoryRepository):
    users = dict()

    for data_row in read_csv_file(os.path.join(data_path, 'users.csv')):
        username = data_row[1]
        password = generate_password_hash(data_row[2])
        user = User(username, password)
        repo.add_user(user)
        users[data_row[0]] = user
    return users


def load_reviews(data_path: str, repo: MemoryRepository, users):
    for data_row in read_csv_file(os.path.join(data_path, 'reviews.csv')):
        review = make_review(
            review_text=data_row[3],
            user=users[data_row[1]],
            movie=repo.get_movie(int(data_row[2])),
            timestamp=datetime.fromisoformat(data_row[4])
        )
        repo.add_review(review)


def populate(data_path: str, repo: MemoryRepository):
    # Load movies and actors/directors/genres into the repository.
    load_movies_actors_directors_genres(data_path, repo)

    # Load users into the repository.
    users = load_users(data_path, repo)

    # Load reviews into the repository.
    load_reviews(data_path, repo, users)
