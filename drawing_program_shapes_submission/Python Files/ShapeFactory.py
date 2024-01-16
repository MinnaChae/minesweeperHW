"""
Name: Aqueno Nirasmi, Minna Chae, Sarah St. Albin
Assignment: Inheritance, Composition and More Patterns
Class: TCSS 502
"""

from shapes import Circle, Square, Rectangle, Triangle


class ShapeFactory:
    """
    Creates and returns Shape objects for DrawingProgram. All shapes should be created via the ShapeFactory.

    Contains one method: create_shape(), which creates a Shape object of a specified type along with the relevant
    data for creating that Shape.
    """

    @staticmethod
    def create_shape(shape_name, *args):
        """
        Creates a Shape object of a specified type using the relevant data for building that Shape. Returns the Shape.
        :param shape_name: name of the shape object to be created.
        :param *args: variable shape data required based on the type of shape to be created.
        :return: a Circle, Square, Rectangle, or Triangle object.
        """
        if shape_name.lower() == "circle":
            return Circle(*args)
        elif shape_name.lower() == "square":
            return Square(*args)
        elif shape_name.lower() == "rectangle":
            return Rectangle(*args)
        elif shape_name.lower() == "triangle":
            return Triangle(*args)
        else:
            raise ValueError('Shape type is not valid')




