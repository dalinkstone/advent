def decipher(filename: str) -> bool:

    with open(filename, "r") as file:
        for line in file:
            result = line.split(",")
    
            for item in result:
                print(item)


    return False

if __name__ == "__main__":
    decipher("input.txt")
