def decipher(filename: str) -> bool:

    with open(filename, "r") as file:

        result = 0

        for line in file:

            line = line.replace('\n', '')

            jolt = 0
            l = 0

            print(f"This is the current line we are working on {line}")

            while l < len(line):

                r = l + 1

                while r < len(line):

                    possible_max = int(line[l]+line[r])
                    jolt = max(jolt, possible_max)

                    r += 1
                    
                l += 1

            print(f"This is the max jolt we found for this line {jolt}")

            result += jolt

            print(f"This is the result right now {result}")

    print(f"The final result is {result}")

    return False

if __name__ == "__main__":
    decipher("input.txt")
