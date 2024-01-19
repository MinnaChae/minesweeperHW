"""
Aqueno Amalraj, Minna Chae, Sarah St. Albin (Team 1)
TCSS 504 Team Solution to Minesweeper Problem
"""


class Minesweeper:
    """
    Creates an output file of one or more minesweeper fields. Shows how many cells with mines are adjacent to safe
    rooms.

    """
    def __init__(self, input_file, output_file):
        """
        Initialize an instance of Minesweeper.
        :param input_file: the input file to be read and processed.
        :param output_file: the output file to be written to.
        """
        self.input_file = input_file
        self.output_file = output_file

    def run_minesweeper_solution(self):
        """
        Contains the main logic to solve the Minesweeper solution.
        """
        # Open the file with a context manager
        with open(self.input_file, "r") as file:
            # Initialize master array
            fields = []

            # Loop through the file
            while True:
                # Create instances of num_of_rows and field by calling read_field()
                num_of_rows, field = self.read_field(file)

                # If number of rows (lines to read) is zero, then break out of the loop
                if num_of_rows == 0:
                    break

                # Create a processed field by calling process_the_field
                processed_field = self.process_the_field(field)
                # Append the processed field to the fields array
                fields.append(processed_field)

            # Write to the output file
            self.write_to_output(fields)

    def read_field(self, file):
        """
        Creates an unprocessed field using row numbers.
        :param file: the input file
        :return: num_of_rows (int), field (array)
        """
        # Grab the first line of the file and strip any trailing characters
        first_line = file.readline().rstrip()
        # Split into an array of strings (two string numbers)
        rows_cols_nums = first_line.split()
        # Extract the first string number (representing the rows) and turn it into an integer
        num_of_rows = int(rows_cols_nums[0])

        # Create the unprocessed current field using num_of_rows to know how many lines to read
        field = [file.readline().rstrip() for _ in range(num_of_rows)]

        # Return row number and the field
        return num_of_rows, field

    def process_the_field(self, field):
        """
        Processes the entire field and replaces each "safe" cell with the number of mines adjacent to it.
        :param field: the unprocessed field (array)
        :return: processed field (array)
        """
        # Initialize an array for the final processed field
        processed_field = []

        # Loop over the unprocessed field (rows and columns)
        for row in range(len(field)):
            # Initialize a string variable to which to append numbers and mines
            processed_row = ""
            for col in range(len(field[row])):
                # Grab the current cell of the unprocessed field
                cell = field[row][col]
                # Check if it has a mine or if it is a safe cell
                # If it's safe, call count_adjacent_mines
                processed_row += "*" if cell == "*" else str(self.count_adjacent_mines(field, row, col))
            # Append the processed row string variable to the processed field array when done
            processed_field.append(processed_row)

        # Return the processed field when all rows and columns have been processed and appended
        return processed_field

    def count_adjacent_mines(self, field, row, col):
        """
        Counts how many mines are adjacent to safe cells.
        :param field: the current field (array)
        :param row: the row coordinate (int)
        :param col: the column coordinate (int)
        :return: the number of mines (int)
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

        # Return the mine count
        return mine_count

    def write_to_output(self, fields):
        """
        Writes to the output file.
        :param fields: the final master array.
        :return: None
        """
        # Write to the official output file with required formatting
        with open(self.output_file, "w") as output_file:
            field_count = 1
            # Iterate over fields
            for field in fields:
                # Before each field, write "Field #x" followed by newline
                output_file.write(f"Field #{field_count}:\n")
                # Join rows in field on a newline and add a newline at the end
                output_file.write("\n".join(field) + "\n")

                # Add a newline between fields unless it's the last field
                if field_count != len(fields):
                    output_file.write("\n")
                field_count += 1


# Usage
minesweeper_instance = Minesweeper('mines.txt', 'minesweeper_output.txt')
minesweeper_instance.run_minesweeper_solution()