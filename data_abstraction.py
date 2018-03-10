from abc import ABCMeta, abstractmethod


class IReportItem:
    __metaclass__ = ABCMeta

    @property
    @abstractmethod
    def uid(self): pass

    @property
    @abstractmethod
    def date(self): pass

    @property
    @abstractmethod
    def country(self): pass

    @abstractmethod
    def to_string(self): pass
