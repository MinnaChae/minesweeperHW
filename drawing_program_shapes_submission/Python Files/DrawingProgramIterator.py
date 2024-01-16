"""
Name: Aqueno Nirasmi, Minna Chae, Sarah St. Albin
Assignment: Inheritance, Composition and More Patterns
Class: TCSS 502
"""

"""
This class uses the class iterator protocol to iterate through the Shape
array and return a Iterator object.
"""


class DrawingProgramIterator:
    def __init__(self, string):
        """ init with a variable to hold the passed parameter (array) and index int"""
        self.words = string
        self.index = 0

    def __next__(self):
        """ iterates the passed parameter (array) and return into a string format"""
        if self.index == len(self.words):
            raise StopIteration()

        word = self.words[self.index]
        self.index += 1
        return word

    def __iter__(self):
        """ returns an interator object"""
        return self