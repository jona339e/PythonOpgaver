from interfaces import IRequiredPersonInfo
from abc import abstractmethod
# IRequiredPersonInfo

class Person(IRequiredPersonInfo):
    def __init__(self, fname, lname):
        self._fname = fname
        self._lname = lname
    
    @property
    def fname(self):
        return self._fname

    @fname.setter
    def fname(self, value):
        self._fname = value


    @property
    def lname(self):
        return self._lname

    @lname.setter
    def lname(self, value):
        self._lname = value


    def get_full_name(self):
        return self.fname + " " + self.lname
    
    @abstractmethod
    def get_person_role_in_tec(self):
        pass
