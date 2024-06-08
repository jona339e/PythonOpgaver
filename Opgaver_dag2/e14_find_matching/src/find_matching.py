#!/usr/bin/env python3

def find_matching(L, pattern):
    # return a list of the indexes of the elements in L that contains the pattern

    returnList = []
    # we need to call enumerate for the test to pass
    # Here is a description of what it does and how to use it https://www.geeksforgeeks.org/enumerate-in-python/
    for i in range(len(list(enumerate(L)))):
        if pattern in L[i]:
            returnList.append(i)
    

    return returnList

def main():
    pass

if __name__ == "__main__":
    print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))
    main()
