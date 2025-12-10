def decipher(filename: str) -> int:
    count = 0
    coords = []
    

    with open(filename, "r") as file:
        for line in file:
            coords.append([int(num) for num in line.strip().split(",")])

    for i in range(len(coords)):

        for j in range(i + 1, len(coords)):

            count = max(count, (abs(coords[i][0] - coords[j][0]) + 1) * (abs(coords[i][1] - coords[j][1]) + 1))

    return count


if __name__ == "__main__":
    result = decipher("input.txt")
    print(f"This is the result {result}")
