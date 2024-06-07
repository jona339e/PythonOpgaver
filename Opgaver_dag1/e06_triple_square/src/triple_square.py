#!/usr/bin/env python3

def triple(x):
    return x * 3

def square(x):
    return x ** 2

def main():
    for i in range(1, 11):
        trpl = triple(i)
        sqr = square(i)
        if sqr > trpl:
            break
        print(f"triple({i})=={trpl} square({i})=={sqr}")
    pass

if __name__ == "__main__":
    main()

