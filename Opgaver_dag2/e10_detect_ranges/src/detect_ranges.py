#!/usr/bin/env python3

def detect_ranges(Li):
    LSorted = sorted(Li)
    L = []
    print(LSorted)

    startBuffer = LSorted[0]
    endBuffer = LSorted[0]

    for i in range(1, len(LSorted)):

        # find the ranges
        # if [i] - [i-1] == 1, then it is inside a range
        # if [i] - [i-1] != 1, then it is the end of the range and we can add a touple to L
        # if startbuffer and endbuffer is the same it is not range and we add it to the list

        if i == len(LSorted)-1:
            # if last iteration
            # if startbuffer and endbuffer is the same it is not range and we add it to the list
            # if not we add the last range to the list
            endBuffer = LSorted[i]
            if LSorted[i] - LSorted[i-1] != 1:
                L.append(LSorted[i-1])
                L.append(endBuffer)
            elif startBuffer == endBuffer:
                L.append(LSorted[i])
            else:
                L.append((startBuffer, endBuffer+1))
                
        elif LSorted[i] - LSorted[i-1] == 1:
            endBuffer = LSorted[i]

        else:
            if startBuffer == endBuffer:
                L.append(startBuffer)

            else:
                L.append((startBuffer, endBuffer+1))

            startBuffer = LSorted[i]
            endBuffer = LSorted[i]
        


    return L

def main():
    L = [4, 2, 0, -2, -4]
    result = detect_ranges(L)
    # print(L)
    print(result)

if __name__ == "__main__":
    main()
