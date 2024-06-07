#!/usr/bin/env python3

def distinct_characters(L):
    d = {}
    for w in L:
        d[w] = len(set(w))
    return d

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
