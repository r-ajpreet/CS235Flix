class Actor:

    def __init__(self, actor_full_name: str):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name.strip()
        self.__colleagues = []

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name

    @property
    def colleagues(self):
        return self.__colleagues

    def __repr__(self):
        return f"<Actor {self.__actor_full_name}>"

    def __eq__(self, other):
        return self.__actor_full_name == other.__actor_full_name

    def __lt__(self, other):
        return self.__actor_full_name < other.__actor_full_name

    def __hash__(self):
        return hash(self.__actor_full_name)

    def add_actor_colleague(self, colleague):
        if type(colleague) is Actor:
            if not self.check_if_this_actor_worked_with(colleague):
                self.__colleagues.append(colleague)

    def check_if_this_actor_worked_with(self, colleague):
        if type(colleague) is Actor:
            return colleague in self.__colleagues


class TestActorMethods:

    def test_init(self):
        actor1 = Actor("Angelina Jolie")
        assert repr(actor1) == "<Actor Angelina Jolie>"
        actor2 = Actor("")
        assert actor2.actor_full_name is None
        actor3 = Actor(50)
        assert actor3.actor_full_name is None

    def test_repr(self):
        actor1 = Actor("Angelina Jolie")
        assert actor1.__repr__() == "<Actor Angelina Jolie>"

    def test_eq(self):
        actor1 = Actor("Angelina Jolie")
        actor2 = Actor("Jack Black")
        actor3 = Actor("Angelina Jolie")
        assert actor1.__eq__(actor2) is False
        assert actor1.__eq__(actor3) is True

    def test_lt(self):
        actor1 = Actor("Angelina Jolie")
        actor2 = Actor("Jack Black")
        assert actor1.__lt__(actor2) is True
        assert actor2.__lt__(actor1) is False

    def test_hash(self):
        actor1 = Actor("Angelina Jolie")
        actor2 = Actor("Jack Black")
        actor3 = Actor("Angelina Jolie")
        assert actor1.__hash__() != actor2.__hash__()
        assert actor1.__hash__() == actor3.__hash__()

    def test_add_actor_colleague(self):
        actor1 = Actor("Angelina Jolie")
        actor2 = Actor("Tom Cruise")

        # add new object not of type Actor
        actor1.add_actor_colleague(50)
        assert len(actor1.colleagues) == 0

        # add new colleague
        actor1.add_actor_colleague(actor2)
        assert actor1.colleagues[0] == actor2

        # add existing colleague
        actor1.add_actor_colleague(actor2)
        assert len(actor1.colleagues) == 1

        # add a second colleague
        actor3 = Actor("Chris Pratt")
        actor1.add_actor_colleague(actor3)
        assert len(actor1.colleagues) == 2
        assert actor1.colleagues[1] == actor3

    def test_check_if_this_actor_worked_with(self):
        actor1 = Actor("Angelina Jolie")
        actor2 = Actor("Tom Cruise")
        actor3 = Actor("Chris Pratt")

        actor1.add_actor_colleague(actor2)

        assert actor1.check_if_this_actor_worked_with(actor2) is True
        assert actor1.check_if_this_actor_worked_with(actor3) is False
