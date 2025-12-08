from collections import defaultdict

def decipher(filename: str) -> int:
    with open(filename, "r") as file:
        grid = [line.rstrip() for line in file if line.strip()]

    active_timelines = defaultdict(int)
    start_row_index = 0
    
    for r, row in enumerate(grid):
        if 'S' in row:
            active_timelines[row.index('S')] = 1
            start_row_index = r + 1
            break
            
    total_completed_timelines = 0
    width = len(grid[0]) if grid else 0

    for r in range(start_row_index, len(grid)):
        current_row_str = grid[r]
        next_timelines = defaultdict(int)
        
        for col, count in active_timelines.items():
            if col < 0 or col >= len(current_row_str):
                total_completed_timelines += count
                continue

            char = current_row_str[col]
            
            next_positions = []
            if char == '^':
                next_positions = [col - 1, col + 1]
            elif char == '.':
                next_positions = [col]
            else:
                next_positions = [col]
            
            for next_col in next_positions:
                if 0 <= next_col < width:
                    next_timelines[next_col] += count
                else:
                    total_completed_timelines += count

        active_timelines = next_timelines
        
        if not active_timelines:
            break

    total_completed_timelines += sum(active_timelines.values())

    return total_completed_timelines

if __name__ == "__main__":
    result = decipher("input.txt")
    print(f"This is the result {result}")
