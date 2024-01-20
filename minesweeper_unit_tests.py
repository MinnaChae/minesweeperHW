"""
Name: Aqueno Nirasmi, Minna Chae, Sarah St. Albin
Assignment: Minesweeper
Class: TCSS 504
"""
import unittest
import os
import filecmp
from unittest.mock import patch
from minesweeper_team_solution import Minesweeper


class MinesweeperTests(unittest.TestCase):

    def test_minesweeper_init(self):
        """
        Tests the general functionality of __init__ constructor.
        :return: None
        """
        input_file = "test_input.txt"
        output_file = "test_output.txt"

        minesweeper_instance = Minesweeper(input_file, output_file)

        minesweeper_instance.run_minesweeper_solution()

        # Assert that the attributes are set correctly, object is properly instantiated
        self.assertEqual(minesweeper_instance.input_file, input_file)
        self.assertEqual(minesweeper_instance.output_file, output_file)


    def test_run_minesweeper_solution(self):
        """
        Tests the general functionality of the run_minesweeper_solution method.
        :return: None
        """

        input_file = "test_input.txt"
        output_file = "test_output.txt"

        minesweeper_instance = Minesweeper(input_file, output_file)
        minesweeper_instance.run_minesweeper_solution()

        # Assert that the output is what is expected given the input (the method actually solves the problem)
        self.assertTrue(filecmp.cmp(output_file, "expected_output.txt", shallow=False))

    def test_read_field(self):
        """
        Tests the basic functionality of the read_field method.
        :return: None
        """
        input_file = "test_input.txt"
        output_file = "test_output.txt"

        minesweeper_instance = Minesweeper(input_file, output_file)

        with open(input_file, "r") as input_file:
            # Assertions
            num_of_rows, field = minesweeper_instance.read_field(input_file)
            # Number of rows is grabbed and returned as an integer
            assert isinstance(num_of_rows, int)
            # The field returned is a list
            assert isinstance(field, list)
            # The correct dimensions are returned
            assert len(field) == num_of_rows

    def test_process_the_field(self):
        """
        Tests basic functionality of process_the_field method.
        :return:
        """
        input_file = "test_input.txt"
        output_file = "test_output.txt"

        minesweeper_instance = Minesweeper(input_file, output_file)

        mock_field = ['...**', '.....', '.....', '*....', '.*.*.']

        processed_field = minesweeper_instance.process_the_field(mock_field)

        expected_field = ['001**', '00122', '11000', '*2211', '2*2*1']

        # Assert that process_the_field returns a processed field in the correct format
        self.assertEqual(processed_field, expected_field)

    def test_count_adjacent_mines(self):
        """
        Tests basic functionality of the count_adjacent_mines method.
        :return:
        """
        input_file = "test_input.txt"
        output_file = "test_output.txt"

        minesweeper_instance = Minesweeper(input_file, output_file)

        mock_field = ['...**', '.....', '.....', '*....', '.*.*.']

        test_mine_count = minesweeper_instance.count_adjacent_mines(mock_field, 2, 2)
        expected_mine_count = 0

        # Assert that the number returned is an integer
        self.assertIsInstance(test_mine_count, int, "The returned mine count should be an integer")

        # Assert that the method is counting mines correctly
        self.assertEqual(expected_mine_count, test_mine_count, "The method did not correctly count adjacent mines")

    def test_write_to_output(self):
        """
        Tests basic functionality of write_to_output: it writes to the output file with the correct formatting.
        :return:
        """
        input_file = "test_input_multiple_fields.txt"
        output_file = "test_output_multiple_fields.txt"
        expected_output = "expected_output_multiple_fields.txt"

        minesweeper_instance = Minesweeper(input_file, output_file)

        mock_field = [
            ['*100', '2210', '1*10', '1110'],
            ['**100', '33200', '1*100'],
            ['*'],
            ['0']
        ]

        minesweeper_instance.write_to_output(mock_field)

        with open(output_file, "r") as file:
            output_content = file.read()

        with open(expected_output, "r") as expected_file:
            expected_content = expected_file.read()

        self.assertEqual(output_content, expected_content)

    def test_given_minefield_proper_formatting(self):
        """
        Tests that a minefield is formatted properly.
        """
        input_file = "test_input.txt"
        output_file = "test_output.txt"
        expected_output = "expected_output.txt"

        minesweeper_instance = Minesweeper(input_file, output_file)

        minesweeper_instance.run_minesweeper_solution()

        with open(output_file, "r") as file:
            formatted_minefield = file.read()
            first_line = file.readline()

        with open(expected_output, "r") as expected_file:
            expected_minefield = expected_file.read()
            expected_first_line = expected_file.readline()

        # Assert that first line of numbers is replaced with "Field #"
        self.assertEqual(first_line, expected_first_line)

        # Assert that all the safe rooms have integers in them and not "."
        for actual_row, expected_row in zip(formatted_minefield, expected_minefield):
            for actual_cell, expected_cell in zip(actual_row.strip(), expected_row.strip()):
                if expected_cell == ".":
                    # Check that the corresponding actual cell is an integer
                    self.assertTrue(actual_cell.isdigit(), msg=f"Expected integer in cell, got {actual_cell}")

        # Assert that overall formatting is correct
        self.assertEqual(formatted_minefield, expected_minefield)



if __name__ == '__main__':
    unittest.main()