"""
Name: Aqueno Nirasmi, Minna Chae, Sarah St. Albin
Assignment: Minesweeper
Class: TCSS 504
"""
import unittest
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

        # Assert that the attributes are set correctly
        self.assertEqual(minesweeper_instance.input_file, input_file)
        self.assertEqual(minesweeper_instance.output_file, output_file)

        # Assert that the output is what is expected given the input
        self.assertTrue(filecmp.cmp(output_file, "expected_output.txt", shallow=False))

    def test_run_minesweeper_solution(self):
        """
        Tests the general functionality of the run_minesweeper_solution method.
        :return: None
        """

        input_file = "test_input.txt"
        output_file = "test_output.txt"

        mock_field = ['...**', '.....', '.....', '*....', '.*.*.']

        minesweeper_instance = Minesweeper(input_file, output_file)

        with patch.object(minesweeper_instance, 'read_field') as mock_read_field:
            mock_read_field.return_value = (5, mock_field)

        with patch.object(minesweeper_instance, 'process_the_field') as mock_process_the_field:
            pass

        with patch.object(minesweeper_instance, 'write_to_output') as mock_write_to_output:
            pass

            minesweeper_instance.run_minesweeper_solution()

            mock_read_field.assert_called()

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
 
def test_read_col_row_data_single_minefield(self):
        """
        Testing the input read for Minefield row, col, and data
        """
        with open('minefield.txt', 'r') as file:
            first_line = file.readline().rstrip()
            expected_row, expected_col = first_line.split()
            expected_row = int(expected_row)
            expected_col = int(expected_col)
            expected_data = [file.readline().rstrip() for _ in range(expected_row)]

        ms = Minesweeper('minefield.txt', 'minesweeper_output.txt')

        with open('minefield.txt', 'r') as file:
            row_count, data = ms.read_field(file)
        col_count = len(data)
        self.assertEqual(expected_row, row_count, "Testing for input of rows")
        self.assertEqual(expected_col, col_count, "Testing for input of col")
        self.assertEqual(expected_data, data, "Testing for input of data")

    # def test_write_to_output(self):
    #     """
    #     Tests basic functionality of write_to_output.
    #     :return:
    #     """
    #     input_file = "test_input.txt"
    #     output_file = "test_output.txt"
    #
    #     mock_processed_field = [['001**', '00122', '11000', '*2211', '2*2*1']]
    #
    #     with patch("builtins.open", mock_open()) as mock_file:
    #         minesweeper_instance = Minesweeper(input_file, output_file)
    #         minesweeper_instance.write_to_output(mock_processed_field)
    #
    #         calls = [mock.call(output_file, "w")]
    #
    #         # Assert that open was called with correct args
    #         mock_file.assert_has_calls(calls, any_order=False)
    #         # Assert that write was called
    #         mock_file().write.assert_called()
    #
    #         # Get the content written to the file
    #         written_content = mock_file().write.call_args[0][0]
    #
    #         # Assert that the content matches the expected format
    #         expected_content = "Field #1:\n001**\n00122\n11000\n*2211\n2*2*1\n"
    #         self.assertEqual(written_content, expected_content)



if __name__ == '__main__':
    unittest.main()
