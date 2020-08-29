class Director:

    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()

    @property
    def director_full_name(self) -> str:
        return self.__director_full_name

    def __repr__(self):
        return f"<Director {self.__director_full_name}>"

    def __eq__(self, other):
        return self.__director_full_name == other.__director_full_name

    def __lt__(self, other):
        return self.__director_full_name < other.__director_full_name

    def __hash__(self):
        return hash(self.__director_full_name)


class TestDirectorMethods:

    def test_init(self):
        director1 = Director("Taika Waititi")
        assert repr(director1) == "<Director Taika Waititi>"
        director2 = Director("")
        assert director2.director_full_name is None
        director3 = Director(42)
        assert director3.director_full_name is None

    def test_repr(self):
        director1 = Director("Taika Waititi")
        assert director1.__repr__() == "<Director Taika Waititi>"

    def test_eq(self):
        director1 = Director("Taika Waititi")
        director2 = Director("Taika Waititi")
        assert director1.__eq__(director2) is True

    def test_lt(self):
        director1 = Director("Taika Waititi")
        director2 = Director("James Cameron")
        assert director1.__lt__(director2) is False
        assert director2.__lt__(director1) is True

    def test_hash(self):
        director1 = Director("Taika Waititi")
        director2 = Director("James Cameron")
        director3 = Director("Taika Waititi")
        assert director1.__hash__() != director2.__hash__()
        assert director1.__hash__() == director3.__hash__()
