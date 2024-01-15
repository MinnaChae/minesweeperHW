""" Name: Aqueno Nirasmi Amalraj
    Assignment: Minesweeper """
import os

input_file = open('mines.txt', 'r')
output_file = open('minesweeper_output.txt', 'w')
lines = input_file.readlines()
field_string = "Field #"
field_num = 1
num_of_lines = len(lines)
line_num = 0


def find_adjacent_mines(row, col):
    """ This method is a helper method used in display_output method to print the values
     param1: row
     param2: col
     return: returns value which helps to find mines, if a mine is found on the adjacent square
     then the value of this square is incremented """
    count = 0  # initialize count
    r = row - 1  # index starts from 0 so decrement row by 1 and store it in r
    while r <= row + 1:  # looping condition for row, row-1 and row+1
        if 0 <= r < rows:
            c = col - 1  # same as row for column
            while c <= col + 1:
                if 0 <= c < cols:
                    count = count + int_matrix[r][c]  # increase the count value in int_matrix
                c += 1
        r += 1
    if int_matrix[row][col] == 1:  # initially the mines are represented as 1's now it is changed to *
        return "*"
    return count


def display_output():
    """ This function helps to print the output in matrix using nested for loops """
    s = ""
    for a in range(0, rows):
        for b in range(0, cols):
            s = s + str(find_adjacent_mines(a, b)) + ""

        s += "\n"

    return s + "\n"


while line_num < num_of_lines:
    row_col = lines[line_num].strip()  # strip the row and col and store in row_col
    arr = row_col.split()  # split the string row_col into a list and store in arr
    rows = int(arr[0])  # convert string arr into int
    cols = int(arr[1])
    line_num += 1
    # Create a 2D input_matrix to convert the input from the input file to string
    input_matrix = [["" for _ in range(cols)] for _ in range(rows)]
    # Create another 2D matrix to convert the string input to string "1"s(mines) and "0"s(safe space)
    string_int_matrix = [["" for _ in range(cols)] for _ in range(rows)]

    if 0 < rows <= 100 and 0 < cols <= 100:  # check if rows and cols are inbetween the given range
        for i in range(rows):
            line = lines[line_num].strip()  # strip every line and store in a variable called line
            for j in range(cols):
                input_matrix[i][j] = line[j]  # store the input strings in input_matrix
                if input_matrix[i][j] == "*":  # if the input_matrix in "*" change it to "1"
                    string_int_matrix[i][j] = "1"  # and store in string_int_matrix
                if input_matrix[i][j] == ".":  # change "." to "0"
                    string_int_matrix[i][j] = "0"

            line_num += 1

        if row_col:  # condition for printing Field number
            output_file.write(field_string + str(field_num) + ":" + "\n")
            # print(field_string + str(field_num) + ":")

            field_num += 1
        # Create 2D matrix to convert string 1's and 0's to integer 1 and 0
        int_matrix = [[int(ele) for ele in sub] for sub in string_int_matrix]
        # display_output()
        output_file.write((display_output()))
    else:
        break

input_file.close()  # close input_file
output_file.close()  # close output_file

# to remove the additional line on the output_file
with open('minesweeper_output.txt', 'rb+') as filehandle:
    filehandle.seek(-2, os.SEEK_END)
    filehandle.truncate()
