def decipher(filename: str) -> int:
    count = 0
    col_start = 0

    with open(filename, "r") as file:
        lines = file.readlines()

    max_len = max(len(line.strip()) for line in lines)

    inputs = [line.strip().ljust(max_len + 1) for line in lines]

    for col in range(max_len + 1):
        if all(line[col] == " " for line in inputs):
            problem = [line[col_start:col] for line in inputs]

            operator = problem.pop().strip()

            columns = zip(*problem)

            terms = ["".join(col).strip() for col in columns]

            count += eval(operator.join(terms))

            col_start = col + 1

    return count


if __name__ == "__main__":
    result = decipher("input.txt")
    print(f"This is the result {result}")
