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

            rangeToAdd = range(int(thisRange[0]), int(thisRange[1])+1)

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

        ranges.sort(key=lambda x: x.start)

        final_ranges = []

        curr_start, curr_stop = ranges[0].start, ranges[0].stop

        for i in range(1, len(ranges)):

            next_range = ranges[i]

            if next_range.start < curr_stop:
                 curr_stop = max(curr_stop, next_range.stop)
            else:
                final_ranges.append(range(curr_start, curr_stop))
                curr_start, curr_stop = next_range.start, next_range.stop

        final_ranges.append(range(curr_start, curr_stop))

        for ranger in final_ranges:

            count += ranger.stop - ranger.start


    return count

if __name__ == "__main__":
    result = decipher("input.txt")
    print(f"\nThis is the result: {result}")
