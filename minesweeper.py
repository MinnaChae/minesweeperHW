"""
Minna Chae
TCSS 504
A0: Warmup/Readiness
"""

""" This program takes an input and produces a file displaying the game Minefield.
 The input "mines.txt" is an assortment of symbols displaying . and * to indicate a mine or no mine. The txt
 also consists of the playing areas dimension.
 
 The output of this program "minesweeper_output.txt" will indicate the field number and display * for mines
 and numbers for the number of mines around that coordinate.
 """

class Minefield:

    def __init__(self):
        self.__input_symbols = {}
        self.__mine_field = {}
        self.__rows = 0
        self.__cols = 0
        self.__field = 0
        self.__output_file = open('minesweeper_output.txt', 'w')
        self.__input_file = open('mines.txt', 'r')

    def read_input(self):
        """
        Reads the input and calls other functions to create the output
        """
        lines_to_read = self.__input_file.readline()
        row, col = lines_to_read.split()
        self.__rows = int(row)
        self.__cols = int(col)
        str_print = ""
        while self.__rows != 0:
            for i in range(self.__rows):
                data = self.__input_file.readline().strip('\n')
                col = 0
                for letters in data:
                    str_print += letters
                    self.__input_symbols[(i, col)] = letters
                    col += 1
                str_print = ""
            self.create_layout()
            self.output_write()
            lines_to_read = self.__input_file.readline()
            row, col = lines_to_read.split()
            self.__rows = int(row)
            self.__cols = int(col)
        self.__input_file.close()
        self.__output_file.close()

    def create_layout(self):
        """
        Creates the minefield layout
        """
        for r in range(0, self.__rows):
            for c in range(0, self.__cols):
                if self.__input_symbols[r, c] == '*':
                    self.__mine_field[r, c] = '*'
                else:
                    self.__mine_field[r, c] = self.view_area(r, c)

    def view_area(self, ori_row, ori_col):
        """
        Views the 8 surrounding values to determine how many mines are around the current
        position. Count keeps track of the position with the number of surrounding mines
        return: int
        """
        count = 0
        # upper left
        if ori_row > 0 and ori_col > 0:
            if self.__input_symbols[(ori_row - 1, ori_col - 1)] == "*":  # upper left
                count += 1
        if ori_row > 0:
            if self.__input_symbols[(ori_row - 1, ori_col)] == "*":  # directly up
                count += 1
            if ori_col + 1 < self.__cols:
                if self.__input_symbols[(ori_row - 1, ori_col + 1)] == "*":  # upper right
                    count += 1
        if ori_col > 0:
            if self.__input_symbols[(ori_row, ori_col - 1)] == "*":  # left
                count += 1
            if ori_row + 1 < self.__rows:
                if self.__input_symbols[(ori_row + 1, ori_col - 1)] == "*":  # below left
                    count += 1
        if ori_col + 1 < self.__cols:
            if self.__input_symbols[(ori_row, ori_col + 1)] == "*":  # right
                count += 1
            if ori_row + 1 < self.__rows:
                if self.__input_symbols[(ori_row + 1, ori_col + 1)] == "*":  # below right
                    count += 1
        if ori_row + 1 < self.__rows:
            if self.__input_symbols[(ori_row + 1, ori_col)] == "*":  # directly below
                count += 1
        return count

    def output_write(self):
        """
        Put the minefield to the output file
        """
        self.__field += 1
        str_print = ""
        self.__output_file.write('Field #' + str(self.__field) + ':' + '\n')
        for r in range(0, self.__rows):
            for c in range(0, self.__cols):
                str_print += str(self.__mine_field[r, c])
            self.__output_file.write(str_print + '\n')
            str_print = ""
        self.__output_file.write('\n')


m = Minefield()
m.read_input()
