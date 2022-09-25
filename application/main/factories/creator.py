from abc import abstractmethod, ABC


class Creator(ABC):
    """
    Provide class should be used for factory
    """

    @abstractmethod
    def concrete(self):
        pass

    """
    Operation should be executed if any
    """

    def generate_with_data(self, data: tuple):
        pass
