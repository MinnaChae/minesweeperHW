import random



def create_minefield(rows, columns, mine_percentage):
    minefield = [['.' for _ in range(columns)] for _ in range(rows)]

    total_cells = rows * columns
    num_mines = int((mine_percentage / 100) * total_cells)

    mine_locations = random.sample(range(total_cells), num_mines)

    for location in mine_locations:
        row = location // columns
        col = location % columns
        minefield[row][col] = '*'

    return minefield



def write_to_file(rows, columns, minefield, filename):
    with open(filename, 'w') as file:
        file.write(f"{rows} {columns}\n")
        for row in minefield:
            file.write(''.join(row) + '\n')






def main():

    filename = 'minefield.txt'

    while True:


        rows = int(input("Enter the number of rows: "))
        columns = int(input("Enter the number of columns: "))
        mine_percentage = float(input("Enter the percentage of mines (0-100): "))


        minefield = create_minefield(rows, columns, mine_percentage)


        write_to_file(rows, columns, minefield, filename)


        another_minefield = input("Do you want to enter data for another minefield? (yes/no): ").lower()
        if another_minefield != 'yes':
            break

        



if __name__ == "__main__":
    main()
