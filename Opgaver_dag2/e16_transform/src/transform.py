#!/usr/bin/env python3

def transform(s1, s2):

    # z = list(zip(list(map(int, s1.split())), list(map(int, s2.split()))))
    # print(z[0])
    # print(z[1])

    return list(map(lambda x: x[0] * x[1], zip(list(map(int, s1.split())), list(map(int, s2.split())))))

def main():
    print(transform("1 5 3", "2 6 -1")) # [2, 30, -3]
    pass

if __name__ == "__main__":
    main()
