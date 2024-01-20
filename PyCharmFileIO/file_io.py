
"""
Input file format is as follows:

three integers
two strings (occurs 1 or more times)

EXAMPLE
1 2 3
hello goodbye
yes no
true false
happy happier
"""

#open file for input (reading mode)
#if file is in same location as source (Python) code you only have to specify file name and not path
input_file = open('input.txt', 'r')

#open file for output (writing mode)
#to view output file in PyCharm once it is created (after running program), right click on your project folder
# then choose Reload from Disk
output_file = open('output.txt', 'w')

#grab first line of input from file
first_line = input_file.readline()

#separate the values, there are three ints as per specs above
int1, int2, int3 = first_line.split()
print('type of int1 is an int?: ', isinstance(int1, int))

#they are strings at first so make them ints
int1 = int(int1)
int2 = int(int2)
int3 = int(int3)
print('type of int1 is an int?: ', isinstance(int1, int))

#let's write those numbers to the output file
#the write function only likes strings, so we have to change our ints back into string data
#plus we need to include a newline (\n) at end of write
output_file.write('the ints are: ' + str(int1) + ', ' + str(int2) + ', ' + str(int3) + '\n')

#now read the strings from the input file one at a time and write to output file
# for line in input_file:
#     str1, str2 = line.split()
#     output_file.write('the two strings just read are: ' + str1 + ', ' + str2 + '\n')

#here is another way to do the same thing done in for loop above
line = input_file.readline()
while line:
    str1, str2 = line.split()
    output_file.write('The two strings just read are: ' + str1 + ', ' + str2 + '\n')
    line = input_file.readline()

#always close your files when done working with them!
input_file.close()
output_file.close()
