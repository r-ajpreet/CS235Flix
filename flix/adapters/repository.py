import abc
from typing import List
from datetime import date

from flix.domain.model import #TODO


repo_instance = None


class RepositoryException(Exception):

    def __init__(self, message=None):
        pass


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def #TODO