def decipher(filename: str) -> bool:

    invalidIdResult = 0

    with open(filename, "r") as file:
        for line in file:
            lineResult = line.split(",")
    
            for item in lineResult:
                rangeResult = item.split("-")
                
                searchRange = range(int(rangeResult[0]), int(rangeResult[1])+1)

                print(f"This is the current search range {searchRange}")

                for num in searchRange:

                    strNum = str(num)

                    lenNum = len(strNum)

                    if lenNum == 1:
                        continue

                    for patternLen in range(1, (lenNum // 2) + 1):
                        
                        if lenNum % patternLen == 0:
                            pattern = strNum[:patternLen]

                            possibleMatch = pattern * (lenNum // patternLen)

                            if strNum == possibleMatch:
                                print(f"This is the match {strNum}")

                                invalidIdResult += num
                                break




    print(f"The new count is {invalidIdResult}")
    
    return False

if __name__ == "__main__":
    decipher("input.txt")
