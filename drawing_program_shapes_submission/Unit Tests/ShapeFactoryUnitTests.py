"""
Name: Aqueno Nirasmi, Minna Chae, Sarah St. Albin
Assignment: Inheritance, Composition and More Patterns
Class: TCSS 502
"""

import unittest
from ShapeFactory import ShapeFactory
from shapes import Circle, Square, Triangle, Rectangle


class TestShapeFactory(unittest.TestCase):
    def test_create_circle(self):
        circle = ShapeFactory.create_shape("Circle", 5)
        self.assertIsInstance(circle, Circle)

    def test_create_square(self):
        square = ShapeFactory.create_shape("Square", 4)
        self.assertIsInstance(square, Square)

    def test_create_rectangle(self):
        rectangle = ShapeFactory.create_shape("Rectangle", 4, 6)
        self.assertIsInstance(rectangle, Rectangle)

    def test_create_triangle(self):
        triangle = ShapeFactory.create_shape("Triangle", 3, 4, 5)
        self.assertIsInstance(triangle, Triangle)

    def test_invalid_shape(self):
        with self.assertRaises(ValueError):
            ShapeFactory.create_shape("InvalidShape", 5)