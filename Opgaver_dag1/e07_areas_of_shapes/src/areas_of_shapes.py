#!/usr/bin/env python3

import math


def main():
    # enter you solution here
    while(True):
        shapes = ["triangle", "rectangle", "circle"]
        inp = input(f"Choose a shape ({shapes[0]}, {shapes[1]}, {shapes[2]}): ")
        if inp.strip() == "":
            break
        if inp not in shapes:
            print("Unknown shape!")
            continue

        if(inp == shapes[0]):
            base = float(input("Give base of the triangle: "))
            height = float(input("ive height of the triangle: "))
            area = 0.5 * base * height
            print(f"The area is {area}")
        elif(inp == shapes[1]):
            width = float(input("Give width of the rectangle: "))
            height = float(input("Give height of the rectangle: "))
            area = width * height
            print(f"The area is {area}")
        elif(inp == shapes[2]):
            radius = float(input("Give radius of the circle: "))
            area = math.pi * radius ** 2
            print(f"The area is {area}")
        



    pass

if __name__ == "__main__":
    main()
