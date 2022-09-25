from abc import abstractmethod, ABC


class Creator(ABC):

    """
    Provide class should be used for factory
    """

    @abstractmethod
    def concrete(self):
        pass

    def get(self):
        return self.concrete()

    """
    Operation should be executed if any
    """

    def operation(self):
        pass
