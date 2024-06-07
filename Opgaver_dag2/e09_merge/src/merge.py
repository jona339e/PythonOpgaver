#!/usr/bin/env python3

def merge(L1, L2):
    L1Buffer = L1.copy()
    L2Buffer = L2.copy()
    L = []
    # Merge L1 and L2 into L
    # [1, 5, 9, 12] [2, 6, 10] => [1, 2, 5, 6, 9, 10, 12]
    # the lists are always sorted ascending
    while(True):
        #if buffer is empty then add the rest of the other buffer and break loop
        if len(L1Buffer) == 0:
            L.extend(L2Buffer)
            break
        elif len(L2Buffer) == 0:
            L.extend(L1Buffer)
            break
        #if first element of buffer is smaller than the other buffer then add it to L. then remove index 0 from buffer
        if L1Buffer[0] < L2Buffer[0]:
            L.append(L1Buffer[0])
            L1Buffer.pop(0)
        else:
            L.append(L2Buffer[0])
            L2Buffer.pop(0)

    return L

def main():
    pass

if __name__ == "__main__":
    main()
