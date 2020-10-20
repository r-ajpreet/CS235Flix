import csv
import os
from datetime import date, datetime
from typing import List

from bisect import bisect, bisect_left, insort_left

from werkzeug.security import generate_password_hash

from flix.adapters.repository import AbstractRepository, RepositoryException
from flix.domain.model import #TODO


class MemoryRepository(AbstractRepository):
    # ?????

    def __init__(self):
        #TODO