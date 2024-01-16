"""
Name: Aqueno Nirasmi, Minna Chae, Sarah St. Albin
Assignment: Dungeon Adventure Game
Class: TCSS 502
"""

import unittest
from unittest import TestCase, mock
from unittest.mock import patch, Mock
from room import Room
from Dungeon import Dungeon
import random

class DungeonTests(unittest.TestCase):

    def test_init(self):
        """Tests the __init__ constructor."""
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        self.assertEqual(dungeon.get_row_length(), rows)
        self.assertEqual(dungeon.get_col_length(), cols)

        self.assertEqual(len(dungeon.get_maze_array()), rows)
        self.assertEqual(len(dungeon.get_maze_array()), cols)

        for row in dungeon.get_maze_array():
            self.assertEqual(len(row), 5)
            for room in row:
                self.assertIsInstance(room, Room)

        self.assertNotEqual(len(dungeon.get_maze_dictionary()), 0)

    @patch('Dungeon.Dungeon._place_items')
    @patch('Dungeon.Dungeon._place_pillars')
    @patch('Dungeon.Dungeon._is_traversable')
    @patch('Dungeon.Dungeon._make_impassable')
    @patch('Dungeon.Dungeon._set_entrance_exit')
    @patch('Dungeon.Dungeon._create_maze')
    def test_build_dungeon(self, mock_create_maze, mock_set_entrance_exit, mock_make_impassable, mock_is_traversable,
                           mock_place_pillars, mock_place_items):
        """ Tests the build_dungeon method. Verifies that the starting row and column are successfully chosen,
        the _create_maze method is called, the entrance and exit are set, some rooms are set as impassable,
        the maze is traversed and if traversable is set as traversable, that self.__items is populated with
        coordinates and Room objects, pillars and items are placed, and if the maze is not traversable then
        it is regenerated. """
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        random.seed(42)

        dungeon.build_dungeon()

        random.seed(42)

        start_row = random.randint(0, rows - 1)
        start_col = random.randint(0, cols - 1)
        start_room = dungeon.get_maze_array()[start_row][start_col]

        mock_create_maze.assert_called_with(start_room, start_row, start_col)

        mock_set_entrance_exit.assert_called()

        mock_make_impassable.assert_called()

        random.seed(42)

        mock_is_traversable.return_value = True

        expected_items = {(row, col): dungeon.get_maze_array()[row][col] for row in range(rows) for col in range(cols)}
        self.assertEqual(dungeon.get_maze_dictionary(), expected_items)
        mock_place_pillars.assert_called()
        mock_place_items.assert_called()

        mock_is_traversable.return_value = False
        mock_create_maze.assert_called_with(start_room, start_row, start_col)

    def test_get_entrance(self):
        """ Verifies that the entrance of the Dungeon's maze is returned. """
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        result = dungeon.get_entrance()
        self.assertEqual(result, dungeon.get_maze_array()[0][0])

    def test_get_maze_array(self):
        """ Verifies that the list of Rooms is returned. """
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        result = dungeon.get_maze_array()
        self.assertEqual(result, dungeon.get_maze_array())

    def test_get_room_str(self):
        """ Verifies that method returns the Room value associated with its location coordinates. """
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        key = (1, 0)
        result = dungeon.get_room_str(key)
        self.assertEqual(result, dungeon.get_maze_dictionary().get(key))

    def test_get_col_length(self):
        """ Verifies that the number of columns in the maze is returned. """
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        result = dungeon.get_col_length()
        self.assertEqual(result, cols)

    def test_get_row_length(self):
        """ Verifies that the number of rows in the maze is returned. """
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        result = dungeon.get_row_length()
        self.assertEqual(result, rows)

    def test_get_doors_north(self):
        """ Verifies that method gets attributes of a Room using North door. """
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        current = (1, 0)
        next = (0, 0)
        direction = "N"
        is_current_room_north_door = dungeon.get_room_str(current).get_north_door()
        is_next_room_north_door = dungeon.get_room_str(next).get_south_door()
        results = dungeon.get_doors(current, next, direction)

        if is_current_room_north_door and is_next_room_north_door:
            self.assertTrue(results, "Test get doors north true failed")
        else:
            self.assertFalse(results, "Test get doors north false failed")

    def test_get_doors_south(self):
        """ Verifies that method gets attributes of a Room using South door. """
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        current = (1, 1)
        next = (2, 1)
        direction = "S"
        is_current_room_north_door = dungeon.get_room_str(current).get_south_door()
        is_next_room_north_door = dungeon.get_room_str(next).get_north_door()
        results = dungeon.get_doors(current, next, direction)

        if is_current_room_north_door and is_next_room_north_door:
            self.assertTrue(results, "Test get doors south true failed")
        else:
            self.assertFalse(results, "Test get doors south false failed")

    def test_get_doors_east(self):
        """ Verifies that method gets attributes of a Room using East door. """
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        current = (1, 1)
        next = (1, 2)
        direction = "E"
        is_current_room_north_door = dungeon.get_room_str(current).get_east_door()
        is_next_room_north_door = dungeon.get_room_str(next).get_west_door()
        results = dungeon.get_doors(current, next, direction)

        if is_current_room_north_door and is_next_room_north_door:
            self.assertTrue(results, "Test get doors east true failed")
        else:
            self.assertFalse(results, "Test get doors east false failed")

    def test_get_doors_west(self):
        """ Verifies that method gets attributes of a Room using West door. """
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        current = (1, 1)
        next = (1, 0)
        direction = "W"
        is_current_room_north_door = dungeon.get_room_str(current).get_west_door()
        is_next_room_north_door = dungeon.get_room_str(next).get_east_door()
        results = dungeon.get_doors(current, next, direction)

        if is_current_room_north_door and is_next_room_north_door:
            self.assertTrue(results, "Test get doors west true failed")
        else:
            self.assertFalse(results, "Test get doors west false failed")

    def test_set_current_room(self):
        """ Verifies that method sets Room as current. """
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        room = dungeon.get_maze_array()[1][0]
        result = dungeon.set_current_room(room)
        self.assertEqual(result, room.set_current_room(True))

    def test_set_room_empty(self):
        """ Verifies that method sets Room as empty. """
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        room = dungeon.get_maze_array()[1][0]
        result = dungeon.set_room_empty((1, 0), pit=False)
        self.assertEqual(result, room.set_empty_room(True))

    def test_get_room_contents(self):
        """ Verifies that method returns a String representation of the contents of a Room, including an
        empty Room. """
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        mock_items = {(1, 0): {'healing_potion': True, 'vision_potion': False, 'pit': False,
                               'entrance': False, 'exit': False, 'multiple_items': False,
                               'empty_room': False, 'abstraction_pillar': False,
                               'polymorphism_pillar': False, 'inheritance_pillar': False,
                               'encapsulation_pillar': False}}

        with patch.object(dungeon, 'get_maze_dictionary', mock_items):
            result = dungeon.get_room_contents((1, 0))

        self.assertEqual(result, " ")  # Room is empty

    def test_print_dictionary(self):
        """ Verifies that method prints the dictionary."""
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        mock_items = {(1, 0): {'healing_potion': True, 'vision_potion': False, 'pit': False,
                               'entrance': False, 'exit': False, 'multiple_items': False,
                               'empty_room': False, 'abstraction_pillar': False,
                               'polymorphism_pillar': False, 'inheritance_pillar': False,
                               'encapsulation_pillar': False}}

        with mock.patch('builtins.print'):
            with mock.patch.object(dungeon, 'get_maze_dictionary', return_value=mock_items):
                result = dungeon.print_dictionary()

        self.assertEqual(result, None)

    def test_is_valid_room(self):
        """ Verifies that method returns True if Room is valid """
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        row = 1
        col = 0

        result = dungeon.is_valid_room(row, col)
        self.assertEqual(result, True)

    @patch.object(Room, 'set_player_traveled')
    @patch.object(Dungeon, 'get_maze_dictionary')
    def test_set_player_traveled(self, mock_get_maze_dictionary, mock_set_player_traveled):
        """ Tests that method sets the player as having traveled to a particular Room. Mocks self.__items, which
        introduces unpredictability into the method. """
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        key = (1, 0)

        mock_items = {(1, 0): {'healing_potion': True, 'vision_potion': False, 'pit': False,
                               'entrance': False, 'exit': False, 'multiple_items': False,
                               'empty_room': False, 'abstraction_pillar': False,
                               'polymorphism_pillar': False, 'inheritance_pillar': False,
                               'encapsulation_pillar': False}}

        mock_get_maze_dictionary.return_value = mock_items

        dungeon.set_player_traveled(key)

        mock_set_player_traveled.assert_called_once()

    @patch('random.shuffle')
    @patch('random.choice')
    def test_create_maze(self, mock_shuffle, mock_choice):
        """ Verifies that _create_maze generates the maze for the Dungeon. Mocks internal methods
        to control randomness. """
        mock_shuffle.side_effect = lambda x: x[0]
        mock_choice.side_effect = lambda x: x

        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        # Mock the _get_neighbor_coords method to return specific coordinates
        with patch.object(dungeon, '_get_neighbor_coords', side_effect=[(1, 0), (2, 0), (1, 1), (0, 1)]):
            # Mock the is_valid_room method to always return True
            with patch.object(dungeon, 'is_valid_room', return_value=True):
                # Mock the _opposite_direction method to return the opposite direction
                with patch.object(dungeon, '_opposite_direction', side_effect=lambda x: {"N": "S", "S": "N", "E": "W",
                                                                                         "W": "E"}[x]):
                    # Mock the _knock_down_door method to do nothing during the test
                    with patch.object(dungeon, '_knock_down_door', Mock()):
                        # Call the _create_maze method
                        dungeon._create_maze(dungeon.get_maze_array()[0][0], 0, 0)

    def test_get_neighbor_coords(self):
        """ Verifies that method returns the integer coordinates of neighboring Rooms depending on direction."""
        row, col = 5, 5
        dungeon = Dungeon(row, col)

        row = 2
        col = 1
        direction = "N"

        new_row, new_col = dungeon._get_neighbor_coords(row, col, direction)
        self.assertEqual((new_row, new_col), (1, 1))

    def test_opposite_direction(self):
        """ Verifies that method returns the String representation of the opposite direction based on parameter """
        row, col = 5, 5
        dungeon = Dungeon(row, col)

        direction = "N"

        result = dungeon._opposite_direction(direction)
        self.assertEqual(result, {"N": "S", "S": "N", "E": "W", "W": "E"}[direction])

    @patch.object(Room, 'set_north_door')
    def test_knock_down_door_north(self, mock_set_north_door):
        """ Verifies that a north door can be set """
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)
        room = Room()

        dungeon._knock_down_door(room, "N")

        mock_set_north_door.assert_called()

    @patch.object(Room, 'set_south_door')
    def test_knock_down_door_south(self, mock_set_south_door):
        """ Verifies that a south door can be set """
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)
        room = Room()

        dungeon._knock_down_door(room, "S")

        mock_set_south_door.assert_called()

    @patch.object(Room, 'set_east_door')
    def test_knock_down_door_east(self, mock_set_east_door):
        """ Verifies that a east door can be set """
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)
        room = Room()

        dungeon._knock_down_door(room, "E")

        mock_set_east_door.assert_called()

    @patch.object(Room, 'set_west_door')
    def test_knock_down_door_west(self, mock_set_west_door):
        """ Verifies that a west door can be set """
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)
        room = Room()

        dungeon._knock_down_door(room, "W")

        mock_set_west_door.assert_called()

    def test_set_entrance_exit(self):
        """ Verifies that method sets the entrance and exit, including setting them as passable and empty. Also
        tests whether method sets a west door for the entrance and an east door for the exit. """
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        dungeon._set_entrance_exit()

        dungeon.get_maze_array()[0][0].set_entrance(True)
        dungeon.get_maze_array()[rows - 1][cols - 1].set_exit()

        dungeon.get_maze_array()[0][0].set_impasse(False)
        dungeon.get_maze_array()[rows - 1][cols - 1].set_impasse(False)

        dungeon.get_maze_array()[0][0].set_empty_room(True)
        dungeon.get_maze_array()[rows - 1][cols - 1].set_empty_room(True)

        dungeon.get_maze_array()[0][0].set_west_door()
        dungeon.get_maze_array()[rows - 1][cols - 1].set_east_door()

        entrance_row, entrance_col = 0, 0
        exit_row, exit_col = rows - 1, cols - 1

        # Assertions
        self.assertTrue(dungeon.get_maze_array()[entrance_row][entrance_col].get_entrance(),
                        'Entrance should be set at (0, 0)')
        self.assertTrue(dungeon.get_maze_array()[exit_row][exit_col].get_exit(),
                        f'Exit should be set at ({exit_row}, {exit_col})')
        self.assertFalse(dungeon.get_maze_array()[entrance_row][entrance_col].get_impasse(),
                         'Entrance should be passable')
        self.assertFalse(dungeon.get_maze_array()[exit_row][exit_col].get_impasse(),
                         'Exit should be passable')
        self.assertTrue(dungeon.get_maze_array()[entrance_row][entrance_col].get_empty_room(),
                        'Entrance should be empty')
        self.assertTrue(dungeon.get_maze_array()[exit_row][exit_col].get_empty_room(),
                        'Exit should be empty')
        self.assertTrue(dungeon.get_maze_array()[entrance_row][entrance_col].get_west_door(),
                        'Entrance should have a west door')
        self.assertTrue(dungeon.get_maze_array()[exit_row][exit_col].get_east_door(),
                        'Exit should have an east door')

    def test_make_impassable(self):
        """ Tests that method can make some Rooms impassable. Randomness controlled by deterministic seed. """
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        random.seed(42)

        dungeon._make_impassable()

        for row in range(rows):
            for col in range(cols):
                room = dungeon.get_maze_array()[row][col]

                if room.get_impasse():
                    self.assertTrue(room.get_impasse(), f"Room at ({row}, {col}) should have impasse set to True")
                else:
                    self.assertFalse(room.get_impasse(), f"Room at ({row}, {col}) should have impasse set to False")

    def test_is_traversable(self):
        """ Tests that method returns True if maze is found traversable or False if not. """
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        start_row = 0
        start_col = 0

        result = dungeon._is_traversable(start_row, start_col)

        self.assertTrue(isinstance(result, bool), f"Expected boolean, got {type(result)}")

        if result:
            self.assertTrue(dungeon._is_traversable(start_row, start_col))
        else:
            self.assertFalse(dungeon._is_traversable(start_row, start_col))


    def test_traverse_the_maze(self):
        """ Verifies that test_traverse_the_maze traverses the maze and returns True if it finds the exit or
        False if not. """
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        start_row = 0
        start_col = 0

        result = dungeon._traverse_the_maze(start_row, start_col)

        self.assertTrue(isinstance(result, bool), f"Expected boolean, got {type(result)}")

        target_room = dungeon.get_maze_array()[rows - 1][cols - 1]

        if result:
            self.assertTrue(dungeon.is_valid_room(start_row, start_col))
            self.assertTrue(target_room.get_visited())
        else:
            self.assertFalse(result, "Expected _traverse_the_maze to return False")

    def test__str__(self):
        """ Verifies that __str__ method returns a String with information about the entire Dungeon. """
        """
        Testing str function
        """
        d = Dungeon(3,3)

        dungeon_expected = ""
        for row in range(d.get_row_length()):
            for col in range(d.get_col_length()):
                room = d.get_room_str((row,col))
                dungeon_expected += f"Room at ({row}, {col}):"
                dungeon_expected += f"\n  - North Door: {room.get_north_door()}"
                dungeon_expected += f"\n  - South Door: {room.get_south_door()}"
                dungeon_expected += f"\n  - East Door: {room.get_east_door()}"
                dungeon_expected += f"\n  - West Door: {room.get_west_door()}"
                dungeon_expected += f"\n  - Visited: {room.get_visited()}"
                dungeon_expected += f"\n  - Entrance: {room.get_entrance()}"
                dungeon_expected += f"\n  - Exit: {room.get_exit()}"
                dungeon_expected += f"\n  - Impasse: {room.get_impasse()}"
                dungeon_expected += f"\n  - Empty Room: {room.get_empty_room()}"
                dungeon_expected += f"\n  - Abstraction Pillar: {room.set_abstraction_pillar(True)}"
                dungeon_expected += f"\n  - Encapsulation Pillar: {room.set_encapsulation_pillar(True)}"
                dungeon_expected += f"\n  - Inheritance Pillar: {room.set_inheritance_pillar(True)}"
                dungeon_expected += f"\n  - Polymorphism Pillar: {room.set_polymorphism_pillar(True)}"
                dungeon_expected += f"\n  - Healing Potion: {room.set_healing_potion(True)}"
                dungeon_expected += f"\n  - Vision Potion: {room.set_vision_potion(True)}"
                dungeon_expected += f"\n  - Pit: {room.set_pit(True)}"
                dungeon_expected += "\n\n"

        self.assertEqual(dungeon_expected, d.__str__(),"Test Dungeon str failed")

    def test_place_pillars(self):
        """
        Testing for one instance of each pillar polymorphism, inheritance, encapsulation, abstraction within the maze
        """
        d = Dungeon(10,10)
        polymorphism = 0
        inheritance =0
        encapsulation = 0
        abstraction = 0

        for row in range(d.get_row_length()):
            for col in range(d.get_col_length()):
                if d.get_room_contents((row, col)) == "P":
                    polymorphism+=1
                elif d.get_room_contents((row, col)) == "I":
                    inheritance +=1
                elif d.get_room_contents((row, col)) == "E":
                    encapsulation +=1
                elif d.get_room_contents((row, col)) == "A":
                    abstraction +=1
        self.assertEqual(polymorphism, 1, "Polymorphism test fail")
        self.assertEqual(inheritance, 1, "Inheritance test fail")
        self.assertEqual(encapsulation, 1, "Encapsulation test fail")
        self.assertEqual(abstraction, 1, "Abstraction test fail")


    def test_place_items(self):
        """
        Testing that the percentage of items Vision, Health, Multi Items, and Pits are
        within the 30% range as set by random.randint within the function.
        """

        d = Dungeon(25,25)
        healing = 0
        vision =0
        pit = 0
        multi = 0
        other_item =0

        for row in range(d.get_row_length()):
            for col in range(d.get_col_length()):
                if d.get_room_contents((row, col)) == "H":
                    healing+=1
                elif d.get_room_contents((row, col)) == "V":
                    vision +=1
                elif d.get_room_contents((row, col)) == "X":
                    pit +=1
                elif d.get_room_contents((row, col)) == "M":
                    multi +=1
                elif d.get_room_contents((row, col)) == "P":
                    other_item+=1
                elif d.get_room_contents((row, col)) == "I":
                    other_item +=1
                elif d.get_room_contents((row, col)) == "E":
                    other_item +=1
                elif d.get_room_contents((row, col)) == "A":
                    other_item +=1
                elif d.get_room_contents((row, col)) == "i":
                    other_item +=1
                elif d.get_room_contents((row, col)) == "O":
                    other_item +=1
        total_item = healing+vision+pit+multi
        total_avail_rooms = 625 - other_item
        percentage = total_item/total_avail_rooms
        self.assertTrue(.25 < percentage < .35, "Place Item test fail")

    def test_get_maze_dictionary(self):
        """ Tests that the method returns the contents of self.__items, which is mocked to control for
        randomness. """
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        room1 = Room()
        room2 = Room()
        room3 = Room()
        room4 = Room()
        room5 = Room()
        room6 = Room()
        room7 = Room()
        room8 = Room()
        room9 = Room()

        dungeon._Dungeon__items = {(0, 0): room1, (0, 1): room2, (0, 2): room3, (1, 0): room4, (1, 1): room5,
                                   (1, 2): room6, (2, 0): room7, (2, 1): room8, (2, 2): room9}

        result = dungeon.get_maze_dictionary()

        self.assertIsInstance(result, dict)
        self.assertIn((0, 0), result)
        self.assertIn((0, 1), result)
        self.assertIn((0, 2), result)
        self.assertIn((1, 0), result)
        self.assertIn((1, 1), result)
        self.assertIn((1, 2), result)
        self.assertIn((2, 0), result)
        self.assertIn((2, 1), result)
        self.assertIn((2, 2), result)

        self.assertIsInstance(result[0, 0], Room)
        self.assertIsInstance(result[0, 1], Room)
        self.assertIsInstance(result[0, 2], Room)
        self.assertIsInstance(result[1, 0], Room)
        self.assertIsInstance(result[1, 1], Room)
        self.assertIsInstance(result[1, 2], Room)
        self.assertIsInstance(result[2, 0], Room)
        self.assertIsInstance(result[2, 1], Room)
        self.assertIsInstance(result[2, 2], Room)

    def test_get_object_symbols(self):
        """ Tests that method returns a dictionary containing different symbols representing Room contents. Mocks
        self.__items to control for Randomness."""
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        room1 = Room()
        room2 = Room()
        room3 = Room()
        room4 = Room()
        room5 = Room()
        room6 = Room()
        room7 = Room()
        room8 = Room()
        room9 = Room()

        dungeon._Dungeon__items = {(0, 0): room1, (0, 1): room2, (0, 2): room3, (1, 0): room4, (1, 1): room5,
                                   (1, 2): room6, (2, 0): room7, (2, 1): room8, (2, 2): room9}

        result = dungeon._get_object_symbols()
        expected_result = 9

        valid_symbols = {"H", "V", "X", "A", "E", "I", "P", "i", "0", "M", "", }
        for value in result.values():
            self.assertIn(value, valid_symbols)
            self.assertIsInstance(value, str)

        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), expected_result)

        self.assertIn((0, 0), result)
        self.assertIn((0, 1), result)
        self.assertIn((0, 2), result)
        self.assertIn((1, 0), result)
        self.assertIn((1, 1), result)
        self.assertIn((1, 2), result)
        self.assertIn((2, 0), result)
        self.assertIn((2, 1), result)
        self.assertIn((2, 2), result)



if __name__ == '__main__':
    unittest.main()