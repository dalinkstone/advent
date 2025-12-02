def decipher(filename: str) -> bool:

    invalidIdResult = 0

    with open(filename, "r") as file:
        for line in file:
            lineResult = line.split(",")
    
            for item in lineResult:
                rangeResult = item.split("-")
                
                searchRange = range(int(rangeResult[0]), int(rangeResult[1]))

                

    return False

if __name__ == "__main__":
    decipher("input.txt")
