def decipher_count(inputGrid: list, r: int, c: int) -> int:
    
    count = 0

    rows = len(inputGrid)
    cols = len(inputGrid[0])

    for i in [-1, 0, 1]:

        for j in [-1, 0, 1]:

            if i == 0 and j == 0:
                continue

            neighbor_row = r + i
            neighbor_col = c + j

            valid_row = 0 <= neighbor_row < rows
            valid_col = 0 <= neighbor_col < cols

            if valid_row and valid_col:
              if inputGrid[neighbor_row][neighbor_col] == '@':
                   count += 1

    return count 

def decipher_simulate(current_grid: list) -> int:

    rows = len(current_grid)
    cols = len(current_grid[0])

    result = 0

    while True:

        next_grid = [row[:] for row in current_grid]

        changes = 0

        for r in range(rows):

            for c in range(cols):

                if current_grid[r][c] == '@':

                    neighbors = decipher_count(current_grid, r, c)

                    if neighbors <= 3:
                        
                        result += 1

                        next_grid[r][c] = '.'
                        changes += 1

        current_grid = next_grid

        if changes == 0:
            break

    return result


def initialize_grid(filename: str) -> list:

    with open(filename, "r") as file:

        lines = file.readlines()

        grid = [list(line.strip()) for line in lines]

    return grid 

if __name__ == "__main__":
    main_grid = initialize_grid("input.txt")
    final_result = decipher_simulate(main_grid)
    print(f"The final result is {final_result}")
