"""
Name: Aqueno Nirasmi, Minna Chae, Sarah St. Albin
Assignment: Inheritance, Composition and More Patterns
Class: TCSS 502
"""

from DrawingProgramIterator import DrawingProgramIterator
from ShapeFactory import ShapeFactory

"""
This class DrawingProgram takes in a shape object and stores it within a list/collection.
DrawingProgram can add shapes to the list, remove all shapes from the list that match the given shape, 
print all shapes matching a given shape, sort the list alphabetically and then by area, return a Shape given an index, 
or replace based on a given index and new Shape. The iter method uses the class iterator protocol to iterate through the Shape
array and return a Iterator object.
"""


class DrawingProgram:
    def __init__(self):
        """ init with array to hold Shape objects and int to count size"""
        self.__list_shapes = []
        self.size = 0

    def __str__(self):
        """  Returns a string representation of each of the shapes  and each shape will be
            separated from others by a newline"""
        formatted_list = [str(shape) for shape in self.__list_shapes]
        return "\n".join(formatted_list) + "\n"

    def add_shape(self, shape):
        """  Add a Shape object to the array"""
        self.__list_shapes.append(shape)
        self.size += 1

    def remove_shape(self, shape):
        """  Removes ALL shapes objects that match the one passed as a string parameter
            Also returns an integer value to signify how many of that shape was removed"""
        if len(self.__list_shapes) == 0:
            raise IndexError("There are no Shapes in the list")
        else:
            remove_shape_counter = 0
            for inList in self.__list_shapes:
                if inList.get_name().lower() == shape.lower():
                    self.__list_shapes.remove(inList)
                    remove_shape_counter += 1
            self.size -= 1
        return remove_shape_counter

    def print_shape(self, shape):
        """  Prints all Shape objects that match the type of the shape string passed in"""
        if len(self.__list_shapes) == 0:
            raise IndexError("There are no Shapes in the list")
        else:
            string = ""
            for inList in self.__list_shapes:
                if inList.get_name().lower() == shape.lower():
                    string += str(inList) + "\n"
        return string

    def sort_shapes(self):
        """  Sorts the list of Shapes in O(nlogn) for its worst case
            shapes will be sorted first by name, then by area if names are same"""
        if len(self.__list_shapes) == 0:
            raise IndexError("There are no Shapes in the list")
        else:
            self.__list_shapes.sort()

    def get_shape(self, index):
        """  Returns the shape at the specified index within the array"""
        if len(self.__list_shapes) == 0:
            raise IndexError("There are no Shapes in the list")
        elif index >= len(self.__list_shapes) or index < 0 or len(self.__list_shapes) == 0:
            raise IndexError("The given index is out of range")
        else:
            return self.__list_shapes[index]

    def set_shape(self, index, shape):
        """Replaces the shape at the specified index within the array"""
        if len(self.__list_shapes) == 0:
            raise IndexError("There are no Shapes in the list")
        elif index >= len(self.__list_shapes) or index < 0 or len(self.__list_shapes) == 0:
            raise IndexError("Index out of range")
        else:
            self.__list_shapes[index] = shape

    def __iter__(self):
        """ Allows iteration through a list of Shapes"""
        if len(self.__list_shapes) == 0:
            raise IndexError("There are no Shapes in the list")
        else:
            return DrawingProgramIterator(self.__list_shapes)