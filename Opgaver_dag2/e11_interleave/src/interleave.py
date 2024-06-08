#!/usr/bin/env python3

def interleave(*lists):
    L = []

    for sublist in zip(*lists):
        
        for item in sublist:
            L.append(item)
    
    return L


def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
