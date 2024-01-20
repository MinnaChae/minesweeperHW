"""
This example shows how to read a number from a file that specifies how many lines of input
follow. You can use that number to read a specific number of lines quite easily.

Let's assume the input file has the following data (the 0 says there are no more lines of data to read):

2
line1
line2
3
line1
line2
line3
4
line1
line2
line3
line4
0

"""
input_file = open('input2.txt', 'r')
lines_to_read = int(input_file.readline()) #first line of 2
while lines_to_read != 0:
    print('current number of lines to read is:', lines_to_read)
    for i in range(lines_to_read):
        #readline grabs the \n as well so we need to strip it off
        data = input_file.readline().strip('\n')
        print('just read:', data)
    lines_to_read = int(input_file.readline())

input_file.close()
print('done reading from file')
