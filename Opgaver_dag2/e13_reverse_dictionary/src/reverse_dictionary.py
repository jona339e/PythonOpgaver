#!/usr/bin/env python3

def reverse_dictionary(d):
    # create a new dictionary that reverses the key-value pairs of the original dictionary, so the keys become values and values become keys
    returnDict = {}

    # iterate on input dictionary
    for key, value in d.items():
        # iterate through the values in the dictionary
        for val in value:
            # if the value is not in the return dictionary
            # add a new entry with the value as key and key as value
            if val not in returnDict:
                returnDict[val] = [key]
            # if the value is already in the return dictionary
            # append the key to the value that already exists
            else:
                returnDict[val].append(key)


    return returnDict

def main():
    pass

if __name__ == "__main__":
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))
    main()
