def decipher(filename: str) -> bool:

    with open(filename, "r") as file:

        result = 0

        for line in file:

            line = [int(num) for num in line if num.isdigit()]

            possible_max_string = []

            print(f"This is the current line we are working on {line}")

            for i, digit in enumerate(line):

                remaining = len(line) - 1 - i

                while possible_max_string and digit > possible_max_string[-1] and (len(possible_max_string) - 1 + 1 + remaining >= 12):
                    possible_max_string.pop()

                if len(possible_max_string) < 12:
                    possible_max_string.append(digit)

            max_num_found = int("".join(map(str, possible_max_string)))

            print(f"This is the max num we found {max_num_found}")

            result += max_num_found


    print(f"The final result is {result}")

    return False

if __name__ == "__main__":
    decipher("input.txt")
