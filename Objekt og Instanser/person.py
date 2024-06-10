from interfaces import IRequiredPersonInfo
# IRequiredPersonInfo

class Person():
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