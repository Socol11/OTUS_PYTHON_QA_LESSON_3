from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_area(self):
        raise NotImplementedError

    @abstractmethod
    def get_perimeter(self):
        raise NotImplementedError

    def add_area(self, other_figure):
        """The method calculates ot summ of areas of two figures"""
        if not isinstance(other_figure, Figure):
            raise ValueError("Can't add area!!!")
        return self.get_area() + other_figure.get_area()
