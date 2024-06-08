#!/usr/bin/env python3

def detect_ranges(Li):
    # sort the list
    LSorted = sorted(Li)
    L = []
    # print(LSorted)


    # loop through the list and find the ranges and put them in a new list L as a tuple
    # if the range is 1, then just add the number to the list

    i = 0
    while i < len(LSorted):
        if i == len(LSorted) - 1:
            L.append(LSorted[i])
            break

        if LSorted[i] + 1 == LSorted[i + 1]:
            start = LSorted[i]
            while i < len(LSorted) - 1 and LSorted[i] + 1 == LSorted[i + 1]:
                i += 1
            end = LSorted[i]
            L.append((start, end+1))

        else:
            L.append(LSorted[i])
        i += 1
    

    return L

def main():
    L = [88, 89, 90, 92, 93, 94, 95, 96, 97]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()

