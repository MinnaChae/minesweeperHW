"""
Aqueno Amalraj, Minna Chae, Sarah St. Albin (Team 1)
TCSS 504 Team Solution to Minesweeper Problem
"""


class FileHandler:
    """
    Handles file reading and writing for the Minesweeper problem.
    """
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def read_input_file(self):
        with open(self.input_file, "r") as file:
            while True:
                # Grab the numbers from the first line (remove whitespace/newline at the end if any)
                first_line = file.readline().rstrip()

                # Split the string to separate the numbers into a list
                rows_cols_nums = first_line.split()

                # Turn the first number into an integer for number of subsequent lines to process
                num_of_rows = int(rows_cols_nums[0])

                # If there are no lines to read, then don't process (handles 0 0 at end of file)
                if num_of_rows == 0:
                    break

                # Initialize the current field as a list of strings using list comprehension
                # Using _ to show that the int returned by range(num_of_rows) isn't going to be in the list comp
                field = [file.readline().rstrip() for _ in range(num_of_rows)]

            return field

    def write_output_file(self, field):
        with open(self.output_file, "w") as output_file:
            for i in range(len(field)):
                output_file.write(f"Field #{i + 1}:\n")
                output_file.write("\n".join(field[i]) + "\n")

                if i != len(field) - 1:
                    output_file.write("\n")


class MinesweeperSolver:
    """
    Processes the field to be written to the output file.
    """
    def __init__(self, field_count, field):
        self.field_count = field_count
        self.field = field
        self.process_fields(field)

    def process_fields(self, field):
        """
        Processes the entire field and replaces each "safe" cell with the number of mines adjacent to it.
        :param field: a list of strings representing the field being processed
        :return: a processed list that contains the number of mines adjacent to safe cells
        """

        # Initialize a list variable for the field after it's processed
        processed_field = []

        # Loop over each cell (row, col) in the field
        for row in range(len(field)):
            # Initialize string variable, where "*" or the adjacent mine count will go
            processed_row = ""
            for col in range(len(field[row])):
                # Set current cell in the field
                cell = field[row][col]
                # Check if the cell contains a mine
                if cell == "*":
                    # If yes, add it to the processed_row variable
                    processed_row += "*"
                else:
                    # If there's no mine, call count_the_mines to see how many adjacent mines there may be
                    mine_count = self.count_adjacent_mines(field, row, col)
                    # Add the number to processed_row after converting to a string
                    processed_row += str(mine_count)
            # Append the processed row string to the processed field list
            processed_field.append(processed_row)

        # Return the finished processed list
        return processed_field

    def count_adjacent_mines(self, field, row, col):
        """
        Helper method for process_the_field. Counts the number of mines adjacent to a particular cell.
        :param field: the list representing the field being processed
        :param row: row coordinate of a cell in the field
        :param col: column coordinate of a cell in the field
        :return: (int) the number of mines adjacent to a given cell
        """

        # Initialize a mine counter
        mine_count = 0

        # Loop over the neighboring cells (including diagonal neighbors) of the given cell
        # Set ranges to stay within the bounds of the field if we're near one of the edges
        for i in range(max(0, row - 1), min(row + 2, len(field))):
            for j in range(max(0, col - 1), min(col + 2, len(field[0]))):
                # If a mine is found in a neighbor cell...
                if field[i][j] == "*":
                    # Increment mine_count
                    mine_count += 1

        # Return to process_the_field
        return mine_count


class Minesweeper:
    """
    Contains primary logic for Minesweeper problem.
    """
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.file_handler = FileHandler(input_file, output_file)
        self.field_count = 1
        self.solve_minesweeper_problem()

    def solve_minesweeper_problem(self):
        while True:
            data = self.file_handler.read_input_file()

            if not data:
                break

            processed_field = MinesweeperSolver(self.field_count, data)

            self.file_handler.write_output_file(processed_field)

            self.field_count += 1


minesweeper_instance = Minesweeper(input_file="mines.txt", output_file="minesweeper_output.txt")