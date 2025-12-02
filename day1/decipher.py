def read(filename: str) -> bool:

    curLocation = 50
    countCorrect = 0

    with open(filename, "r") as file:
        for line in file:
            firstChar = line[0]
            lineLocation = int(line[1:])

            print(f"{firstChar} : {lineLocation}")

            if firstChar == 'L':
                print(f"This is a left character and the current location is {curLocation}")
                pathToNewLocation = curLocation - lineLocation

                print(f"The calculation for path is {pathToNewLocation}")

                #hits = (curLocation - 1) // 100 - (pathToNewLocation - 1) // 100

                #countCorrect += hits
                if pathToNewLocation < 0 and curLocation == 0:
                    countCorrect += abs(pathToNewLocation // 100) - 1
                    print(f"The new count is {countCorrect}")
                elif pathToNewLocation < 0:
                    countCorrect += abs(pathToNewLocation // 100)

                curLocation = pathToNewLocation % 100
                print(f"The new curLocation is {curLocation}")
                
                if curLocation == 0:
                    countCorrect += 1
                    print(f"The new count is {countCorrect}")

            if firstChar == 'R':
                print(f"This is a right character and the current location is {curLocation}")
                pathToNewLocation = curLocation + lineLocation

                print(f"The calculation for path is {pathToNewLocation}")

                #hits = pathToNewLocation // 100 - curLocation // 100

                #countCorrect += hits

                curLocation = pathToNewLocation % 100
                print(f"The new curLocation is {curLocation}")

                if pathToNewLocation > 100:
                   countCorrect += (pathToNewLocation // 100)
                   print(f"The new count is {countCorrect}")

                elif curLocation == 0:
                    countCorrect += 1
                    print(f"The new count is {countCorrect}")

    print(f"The total count is {countCorrect}")

    return False

def decipher() -> bool:

    return True

if __name__ == "__main__":
    read("input.txt")

