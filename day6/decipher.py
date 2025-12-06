def decipher(filename: str) -> int:
    count = 0
    with open(filename, "r") as file:
        rows = [line.split() for line in file if line.strip()]

        vertical = list(map(list, zip(*rows)))

        for item in vertical:
            operator = item.pop()

            max_length = max(len(num) for num in item)

            if operator == '*':
                aligned = [num.ljust(max_length) for num in item]
            else:
                aligned = [num.rjust(max_length) for num in item]

            new_numbers = []

            for i in range(max_length):
                digits = [num[i] for num in aligned]

                vertical_digits = "".join(digits).strip()

                new_numbers.append(vertical_digits)

            equation = ""

            new_numbers.reverse()

            equation = operator.join(new_numbers)

            print(equation)
            count += eval(equation)

    return count


if __name__ == "__main__":
    result = decipher("input.txt")
    print(f"This is the result {result}")
