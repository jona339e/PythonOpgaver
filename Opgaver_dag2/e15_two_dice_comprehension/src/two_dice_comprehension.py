#!/usr/bin/env python3

def main():
    pairs =[ (i, j) for i in range(1, 7) for j in range(1, 7) if i + j == 5]
    for item in pairs:
        print(item)
    pass

if __name__ == "__main__":
    main()
