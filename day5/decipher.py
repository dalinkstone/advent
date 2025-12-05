def decipher(filename: str) -> int:
    
    with open(filename, "r") as file:

        lines = []
        ranges = []
        #targets = []

        count = 0

        for line in file:

            line = line.strip()

            lines.append(line)

        for lineRange in lines:

            if lineRange == '':
                break;

            thisRange = lineRange.split("-")

            rangeToAdd = range(int(thisRange[0]), int(thisRange[1]))

            ranges.append(rangeToAdd)

        #for target in lines:

        #    if "-" in target or target == '':
         #       continue

          #  targets.append(target)

#        for targeter in targets:
#
 #           for ranger in ranges:
  #              
   #             if ranger.start > int(targeter):
    #                continue
#
 #               print("Checking")
  #              if int(targeter) in ranger:
#
 #                   print(f"This is the target {targeter} and this is the range {ranger}")
  #                  count += 1
   #                 break
        #
        for ranger in ranges:

            print(ranger.stop)
            print(ranger.start)
            print(ranger.stop-ranger.start)

            count += ranger.stop - ranger.start



    return count

if __name__ == "__main__":
    result = decipher("input.txt")
    print(f"\nThis is the result: {result}")
