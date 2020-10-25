from typing import Iterable
import random

from flix.adapters.repository import AbstractRepository
from flix.domain.model import Movie


def get_tag_names(repo: AbstractRepository):
    tags = repo.get_tags()
    tag_names = [tag.tag_name for tag in tags]

    return tag_names


def get_random_movies(quantity, repo: AbstractRepository):
    movie_count = repo.get_number_of_movies()

    if quantity >= movie_count:
        # Reduce the quantity of ranks to generate if the repository has an insufficient number of movies.
        quantity = movie_count - 1

    # Pick distinct and random movies.
    random_ranks = random.sample(range(1, movie_count), quantity)
    movies = repo.get_movies_by_rank(random_ranks)

    return movies_to_dict(movies)


################################################
# Functions to convert dicts to model entities #
################################################

def movie_to_dict(movie: Movie):
    movie_dict = {
        'rank': movie.rank,
        'title': movie.title,
        'year': movie.year,
        'description': movie.description,
        'director': movie.director,
        'actors': movie.actors,
        'genres': movie.genres,
        'runtime_minutes': movie.runtime_minutes,
        'rating': movie.rating,
        'votes': movie.votes,
        'revenue': movie.revenue,
        'metascore': movie.metascore,
        'reviews': movie.reviews
    }
    return movie_dict


def movies_to_dict(movies: Iterable[Movie]):
    return [movie_to_dict(movie) for movie in movies]
