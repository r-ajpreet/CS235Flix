from typing import List

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
        if self.size == 0:
            return None
        elif type(index) is int and 0 <= index < self.size:
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
        return self

    def __next__(self):
        # TODO
        pass


class TestWatchListMethods:

    def test_init(self):
        # TODO
        pass

    def test_add_movie(self):
        # TODO
        pass

    def test_remove_movie(self):
        # TODO
        pass

    def test_select_movie_to_watch(self):
        # TODO
        pass

    def test_size(self):
        # TODO
        pass

    def test_first_movie_in_watchlist(self):
        # TODO
        pass