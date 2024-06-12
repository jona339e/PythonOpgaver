from abc import ABC, abstractmethod
# https://docs.python.org/3/library/abc.html


class IRequiredPersonInfo(ABC):
    @property
    @abstractmethod
    def lname(self):
        pass

    @property
    @abstractmethod
    def fname(self):
        pass

    