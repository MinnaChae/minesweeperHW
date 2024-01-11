"""
Minna Chae
TCSS 504
A0: Warmup/Readiness
"""



def readInput():
    #reading file
    # input_file = open('input.txt', 'r')
    # output_file = open('output.txt', 'w')
    #
    # line = input_file.readline()
    # while line:
    #     for word in line:
    #         str1, str2, str3 = line.split()
    #     output_file.write('Testing ' + str1 + ',' + str2 + '\n')
    #     line = input_file.readline()
    # input_file.close()
    # output_file.close()
    mine_field = []
    rowa, cola = (4, 4)
    # for r in range(0, rows):
        # mine_field.append([r for c in range(0, cols)])
    #
    # for r in range(0, rows):
    #     for j in range(0, cols):
    #         print(mine_field[r][j])


    # list = [[mine_field for i in range(cols)] for j in range(rows)]
    # print("\n" + list)

    input_file = open('mines.txt', 'r')
    lines_to_read = input_file.readline()
    rows, cols = lines_to_read.split()
    row = int(rows)
    while row != 0:
        print('current rows: ', row)
        for i in range(row):
            data = input_file.readline().strip('\n')
            print('just read:', data)
            print('this is i', i)
            col = 0
            for letters in data:
                print(letters)
                mine_field.append(letters)
                col +=1
        print('printing 2d array')

        for r in range(0, rowa):
            for j in range(0, cola):
                print(mine_field[r][j])

        lines_to_read = input_file.readline()
        row, col = lines_to_read.split()
        row = int(row)
    input_file.close()


readInput()
