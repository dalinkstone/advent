def decipher(filename: str) -> int:


    with open(filename, "r") as file:

        for line in file:

            line = [int(num) for num in line if num.isdigit()]

            print(line)


    return 1 

if __name__ == "__main__":
    decipher("input.txt")
