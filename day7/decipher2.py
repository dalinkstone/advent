def decipher(filename: str) -> int:
    # Read all lines first so we can process row by row
    with open(filename, "r") as file:
        # Strip newlines to ensure clean indexing
        grid = [line.rstrip() for line in file if line.strip()]

    split_count = 0
    active_beams = set()

    # 1. Find the starting position 'S'
    start_row_index = 0
    for r, row in enumerate(grid):
        if 'S' in row:
            active_beams.add(row.index('S'))
            # We start processing movement from the row AFTER 'S'
            start_row_index = r + 1
            break
    
    # 2. Iterate through the grid starting from the row below S
    for r in range(start_row_index, len(grid)):
        current_row_str = grid[r]
        next_beams = set()
        
        # Check every column index that currently has an active beam
        for col in active_beams:
            # Safety check: ensure beam hasn't gone off the side of the map
            if col < 0 or col >= len(current_row_str):
                continue

            char = current_row_str[col]

            if char == '^':
                # A split occurs!
                split_count += 1
                
                # The beam hits the splitter and stops.
                # Two NEW beams are created to the left and right for the NEXT row.
                next_beams.add(col - 1)
                next_beams.add(col + 1)
                
            elif char == '.':
                # The beam passes through empty space.
                # It continues to the NEXT row at the same column index.
                next_beams.add(col)
            
            # If it hits anything else, the beam is stopped/absorbed 
            # (though the prompt suggests only . and ^ exist)

        # 3. Update the active beams for the next iteration
        active_beams = next_beams
        
        # Optimization: If all beams have exited or stopped, we can end early
        if not active_beams:
            break

    return split_count


if __name__ == "__main__":
    result = decipher("input.txt")
    print(f"This is the result: {result}")
