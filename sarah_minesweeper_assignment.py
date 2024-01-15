"""
Sarah St. Albin
TCSS 504 - Warmup/Readiness Assignment (Minesweeper)
"""


class Minesweeper:
    """
    Creates an output file of one or more minesweeper fields. Shows how many cells with mines are adjacent to safe
    rooms.

    Contains four methods: an init that initializes an instance of Minesweeper with the input and output files as
    required parameters, minesweeper_solution which contains most of the logic for solving the minesweeper problem,
    process_the_field which processes the entire field and replaces each "safe" cell with the number of mines
    adjacent to it, and count_the_mines (a helper for process_the_field) which counts the number of mines adjacent
    to a particular cell.

    """

    def __init__(self, input_file, output_file):
        """
        Initializes an instance of Minesweeper.
        :param input_file: the file to be read and processed.
        :param output_file: the empty file to be written to.
        """
        self.input_file = input_file  # The input file to be read
        self.output_file = output_file  # The output file to write to
        self.minesweeper_solution()  # Automatically call the solution method upon instantiation

    def minesweeper_solution(self):
        """
        Contains the primary logic for solving the Minesweeper problem. Opens and reads the input file, and handles
        external method calls and final writing to the output file.
        :return: the master array (fields)
        """

        # Use context manager to handle file reading (no need to close the file!)
        with open(self.input_file, "r") as file:

            # Start a master array
            fields = []

            # Start a field counter
            field_count = 1

            # Begin looping through the file, focusing on one minesweeper field at a time
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

                # Process the field and store final version that will be written to output file
                field = self.process_the_field(field)

                # Append the field to the master fields array
                fields.append(field)

                # Increment the field_count variable
                field_count += 1

                # Write to the official output file with required formatting
                with open(self.output_file, "w") as output_file:
                    # Iterate over the range of the length of fields
                    for i in range(len(fields)):
                        # Before each field, write "Field #x" followed by newline (+1 so that we don't start at zero)
                        output_file.write(f"Field #{i + 1}:\n")
                        # Join rows in field on a newline and add a newline at the end
                        output_file.write("\n".join(fields[i]) + "\n")

                        # Add a newline between fields unless it's the last field
                        if i != len(fields) - 1:
                            output_file.write("\n")

        return fields

    def process_the_field(self, field):
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
                    mine_count = self.count_the_mines(field, row, col)
                    # Add the number to processed_row after converting to a string
                    processed_row += str(mine_count)
            # Append the processed row string to the processed field list
            processed_field.append(processed_row)

        # Return the finished processed list
        return processed_field

    def count_the_mines(self, field, row, col):
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


minesweeper_instance = Minesweeper('mines.txt', 'minesweeper_output.txt')
