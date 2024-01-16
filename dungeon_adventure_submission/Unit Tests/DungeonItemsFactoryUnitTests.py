"""
Name: Aqueno Nirasmi, Minna Chae, Sarah St. Albin
Assignment: Dungeon Adventure Game
Class: TCSS 502
"""
import unittest
from unittest.mock import patch
from DungeonItemsFactory import DungeonItemsFactory
from DungeonItems import VisionPotion, HealingPotion, Pit


class TestDungeonItemsFactory(unittest.TestCase):
    def test_create_vision_potion(self):
        vision_potion = DungeonItemsFactory.create_item("V")
        self.assertIsInstance(vision_potion, VisionPotion)

    def test_create_healing_potion(self):
        healing_potion = DungeonItemsFactory.create_item("H", 1, 10)
        self.assertIsInstance(healing_potion, HealingPotion)

    def test_create_pit(self):
        pit = DungeonItemsFactory.create_item("X", 1, 10)
        self.assertIsInstance(pit, Pit)

    def test_create_multiple_items(self):
        # Mocking random.sample to ensure predictable results for the test
        items = ["V", "H", "X"]
        with unittest.mock.patch('random.sample', return_value=items):
            created_items = DungeonItemsFactory.create_multiple_items(1, 10)

        self.assertIsInstance(created_items[0], VisionPotion)
        self.assertIsInstance(created_items[1], HealingPotion)
        self.assertIsInstance(created_items[2], Pit)

if __name__ == '__main__':
    unittest.main()