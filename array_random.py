from random import randint

"""
    Practicing to construct an Array in Python as an instance of a class
    The challenge is to replace the values with random numbers and sum all the values
"""

class Array:
    """Class that creates an Array with None values as default and have different methods."""
    def __init__(self, capacity, fill_value=None):
        self.items = []
        for i in range(capacity):
            self.items.append(fill_value)

    def __len__(self):
        """Returns the length of the Array"""
        return len(self.items)

    def __str__(self):
        """Returns the string representation of the Array items"""
        return str(self.items)

    def __iter__(self):
        """Return the iteration of the elements"""
        self.n = 0
        return iter(self.items)

    def __getitem__(self, index):
        """Return the value of the item in a certain index"""
        return self.items[index]

    def __setitem__(self, index, value):
        """Insert a new value at the given index"""
        self.items[index] = value

    def __next__(self):
        """Replace and return the values of the array with a random number using __next__"""
        if self.n <= self.__len__() - 1:
            self.__setitem__(self.n, randint(1, 100))
            self.n += 1
            return self.items
        else:
            raise StopIteration

    def sum(self):
        """Return the sum of the elements inside the array"""
        self.suma = sum([x for x in self.items])
        return self.suma


