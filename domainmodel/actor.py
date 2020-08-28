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
        if not self.check_if_this_actor_worked_with(colleague):
            self.__colleagues.append(colleague)

    def check_if_this_actor_worked_with(self, colleague):
        return colleague in self.__colleagues


class TestActorMethods:

    def test_init(self):
        actor1 = Actor("Angelina Jolie")
        assert repr(actor1) == "<Actor Angelina Jolie>"

        actor2 = Actor("")
        assert actor2.actor_full_name is None

        actor3 = Actor(50)
        assert actor3.actor_full_name is None

        actor4 = Actor("Jack Black")
        assert actor4.colleagues == []
        actor4.add_actor_colleague(actor3)
        # TODO
