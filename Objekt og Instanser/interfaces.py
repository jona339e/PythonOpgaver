from abc import ABC, abstractmethod
# https://docs.python.org/3/library/abc.html


def IRequiredPersonInfo(object):
    @property
    def lname(self):
        pass

    @property
    def fname(self):
        pass

    @abstractmethod
    def get_full_name(self):
        pass
    