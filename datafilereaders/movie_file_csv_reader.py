import csv
from typing import List

from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.genre import Genre
from domainmodel.director import Director


class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__dataset_of_movies = []
        self.__dataset_of_actors = []
        self.__dataset_of_directors = []
        self.__dataset_of_genres = []

    @property
    def filename(self) -> str:
        return self.__file_name

    @property
    def dataset_of_movies(self) -> List[Movie]:
        return self.__dataset_of_movies

    @property
    def dataset_of_actors(self) -> List[Actor]:
        return self.__dataset_of_actors

    @property
    def dataset_of_directors(self) -> List[Director]:
        return self.__dataset_of_directors

    @property
    def dataset_of_genres(self) -> List[Genre]:
        return self.__dataset_of_genres

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            index = 0
            for row in movie_file_reader:
                # read data of row into variables
                title = row['Title']

                genres_str = row['Genre'].split(",")
                genres = []
                for genre in genres_str:
                    genres.append(Genre(genre))

                year = int(row['Year'])

                description = row['Description']

                director = Director(row['Director'])

                actors_str = row['Actors'].split(",")
                actors = []
                for actor in actors_str:
                    actors.append(Actor(actor))

                runtime = row['Runtime (Minutes)']

                rating = row['Rating']

                votes = row['Votes']

                revenue = row['Revenue (Millions)']

                metascore = row['Metascore']

                # create and populate Movie obj
                movieObj = Movie(title, year)

                for genre in genres:
                    movieObj.add_genre(genre)

                movieObj.description = description

                movieObj.director = director

                for actor in actors:
                    movieObj.add_actor(actor)

                if not runtime == "N/A":
                    movieObj.runtime_minutes = int(runtime)

                if not rating == "N/A":
                    movieObj.rating = float(rating)

                if not votes == "N/A":
                    movieObj.votes = int(votes)

                if not revenue == "N/A":
                    movieObj.revenue = float(revenue)

                if not metascore == "N/A":
                    movieObj.metascore = int(metascore)

                # populate datasets
                self.dataset_of_movies.append(movieObj)

                for actor in actors:
                    if actor not in self.dataset_of_actors:
                        self.dataset_of_actors.append(actor)

                if director not in self.dataset_of_directors:
                    self.dataset_of_directors.append(director)

                for genre in genres:
                    if genre not in self.dataset_of_genres:
                        self.dataset_of_genres.append(genre)

                index += 1


class TestMovieFileCSVReaderMethods:

    def test_init(self):
        filename = '../datafiles/Data1000Movies.csv'
        movie_file_reader = MovieFileCSVReader(filename)
        assert movie_file_reader.filename == '../datafiles/Data1000Movies.csv'
        assert len(movie_file_reader.dataset_of_movies) == 0
        assert len(movie_file_reader.dataset_of_actors) == 0
        assert len(movie_file_reader.dataset_of_directors) == 0
        assert len(movie_file_reader.dataset_of_genres) == 0

    def test_read_csv_file(self):
        filename = '../datafiles/Data1000Movies.csv'
        movie_file_reader = MovieFileCSVReader(filename)
        movie_file_reader.read_csv_file()

        # check dataset sizes
        assert len(movie_file_reader.dataset_of_movies) == 1000
        assert len(movie_file_reader.dataset_of_actors) == 1985
        assert len(movie_file_reader.dataset_of_directors) == 644
        assert len(movie_file_reader.dataset_of_genres) == 20

        # check assigning of all attributes from CSV to Movie obj
        movie = movie_file_reader.dataset_of_movies[0]
        assert movie.title == "Guardians of the Galaxy"
        assert movie.genres == [Genre("Action"), Genre("Adventure"), Genre("Sci-Fi")]
        assert movie.description == "A group of intergalactic criminals are forced " \
                                    "to work together to stop a fanatical warrior " \
                                    "from taking control of the universe."
        assert movie.director == Director("James Gunn")
        assert movie.actors == [Actor("Chris Pratt"),Actor("Vin Diesel"),
                                Actor("Bradley Cooper"),Actor("Zoe Saldana")]
        assert movie.year == 2014
        assert movie.runtime_minutes == 121
        assert movie.rating == 8.1
        assert movie.votes == 757074
        assert movie.revenue == 333.13
        assert movie.metascore == 76
