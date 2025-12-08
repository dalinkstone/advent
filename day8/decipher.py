def decipher(filename: str) -> int:
    with open(filename, "r") as file:
        rows = [[int(num) for num in line.strip().split(",")] for line in file] 
        
    # euclidean_distance = square_root(square(x1-x2)+square(y1-y2)+square(z1-z2))

    print(rows[0])
    print(rows[1])

    num = 0

    for i in range(3):
        num += (rows[0][i] - rows[1][i]) ** 2

    num = num ** 0.5

    print(num)

    count = 0
    return count

if __name__ == '__main__':
    result = decipher('input.txt')
    print(f"The result is {result}")
