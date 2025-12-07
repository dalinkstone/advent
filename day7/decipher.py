count = 0


def decipher(filename: str) -> int:
    with open(filename, "r") as file:
        for line in file:
            print(line)
    return count


if __name__ == "__main__":
    result = decipher("input.txt")

    print(f"This is the result {result}")
