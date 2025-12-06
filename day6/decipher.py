def decipher(filename: str) -> int:
    count = 0
    with open(filename, "r") as file:
        rows = [line.split() for line in file if line.strip()]

        vertical = list(map(list, zip(*rows)))


        for item in vertical:
            operator = item.pop()

            equation = ""

            equation = operator.join(item)

            print(equation)
            count += eval(equation)

    return count


if __name__ == "__main__":
    result = decipher("input.txt")
    print(f"This is the result {result}")
