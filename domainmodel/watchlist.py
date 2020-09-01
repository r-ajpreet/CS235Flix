from typing import List

import pytest

from domainmodel.movie import Movie


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