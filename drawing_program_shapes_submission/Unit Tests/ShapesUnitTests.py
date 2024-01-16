"""
Name: Aqueno Nirasmi, Minna Chae, Sarah St. Albin
Assignment: Inheritance, Composition and More Patterns
Class: TCSS 502
"""

import unittest
from shapes import Circle, Square, Rectangle, Triangle


class TestShapes(unittest.TestCase):
    """ Testing the shape class and its child classes"""
    def test_circle_area_perimeter(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), 78.53981633974483)  # Testing the area of the Circle class
        self.assertAlmostEqual(circle.perimeter(), 31.41592653589793)  # Testing the perimeter of the Circle class
        self.assertEqual(circle.get_name(), "Circle")  # Testing the getter function

    def test_square_area_perimeter(self):
        square = Square(4)
        self.assertEqual(square.area(), 16)  # Testing the area of the Square class
        self.assertEqual(square.perimeter(), 16)  # Testing the perimeter of the Square class
        self.assertEqual(square.get_name(), "Square")  # Testing the getter function

    def test_rectangle_area_perimeter(self):
        rectangle = Rectangle(4, 6)
        self.assertEqual(rectangle.area(), 24)  # Testing the area of the Rectangle class
        self.assertEqual(rectangle.perimeter(), 20)  # Testing the perimeter of the Rectangle class
        self.assertEqual(rectangle.get_name(), "Rectangle")  # Testing the getter function

    def test_triangle_area_perimeter(self):
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.area(), 6)  # Testing the area of the Triangle class
        self.assertEqual(triangle.perimeter(), 12)  # Testing the perimeter of the Triangle class
        self.assertEqual(triangle.get_name(), "Triangle")  # Testing the getter function


if __name__ == '__main__':
    unittest.main()