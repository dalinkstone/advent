def decipher(filename: str) -> int:
    with open(filename, "r") as file:
        grid = [line.rstrip() for line in file if line.strip()]

    split_count = 0
    active_beams = set()

    start_row_index = 0
    for r, row in enumerate(grid):
        if 'S' in row:
            active_beams.add(row.index('S'))
            start_row_index = r + 1
            break
    
    for r in range(start_row_index, len(grid)):
        current_row_str = grid[r]
        next_beams = set()
        
        for col in active_beams:
            if col < 0 or col >= len(current_row_str):
                continue

            char = current_row_str[col]

            if char == '^':
                split_count += 1
                
                next_beams.add(col - 1)
                next_beams.add(col + 1)
                
            elif char == '.':
                next_beams.add(col)
            
        active_beams = next_beams
        
        if not active_beams:
            break

    return split_count


if __name__ == "__main__":
    result = decipher("input.txt")
    print(f"This is the result: {result}")
