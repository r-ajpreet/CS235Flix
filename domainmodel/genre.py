
class Genre:

    def __init__(self, genre_name: str):
        if genre_name == "" or type(genre_name) is not str:
            self.__genre_name = None
        else:
            self.__genre_name = genre_name.strip()

    @property
    def genre_name(self) -> str:
        return self.__genre_name

    def __repr__(self):
        return f'<Genre {self.__genre_name}>'

    def __eq__(self, other):
        return self.__genre_name == other.__genre_name

    def __lt__(self, other):
        return self.__genre_name < other.__genre_name

    def __hash__(self):
        return hash(self.__genre_name)


class TestClassMethods:

    def test_init(self):
        genre1 = Genre("Horror")
        assert repr(genre1) == "<Genre Horror>"
        genre2 = Genre("")
        assert genre2.genre_name is None
        genre3 = Genre(50)
        assert genre3.genre_name is None

    def test_repr(self):
        genre1 = Genre("Horror")
        assert genre1.__repr__() == "<Genre Horror>"

    def test_eq(self):
        genre1 = Genre("Horror")
        genre2 = Genre("Comedy")
        genre3 = Genre("Horror")
        assert genre1.__eq__(genre2) is False
        assert genre1.__eq__(genre3) is True

    def test_lt(self):
        genre1 = Genre("Horror")
        genre2 = Genre("Comedy")
        assert genre1.__lt__(genre2) is False
        assert genre2.__lt__(genre1) is True

    def test_hash(self):
        genre1 = Genre("Horror")
        genre2 = Genre("Comedy")
        genre3 = Genre("Horror")
        assert genre1.__hash__() != genre2.__hash__()
        assert genre1.__hash__() == genre3.__hash__()