from abc import abstractmethod, ABC


class Creator(ABC):
    """
    Provide class should be used for factory
    """

    @abstractmethod
    def concrete(self):
        pass

    """
    Instantiate concrete
    """

    def get(self):
        return self.concrete()()

    """
    Operation should be executed if any
    """

    def get_with_data(self, data: tuple):
        pass
