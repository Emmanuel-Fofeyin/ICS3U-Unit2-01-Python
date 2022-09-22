#!/usr/bin/env python3

# Created by: Emmanuel Fofeyin
# Created on: Sep 2020
# This program calculates the area and perimeter of a circle
#    with radius 15mm

import math


def main():
    # this function calculates the area and perimeter

    print("If a circle has a radius of 15 mm: ")
    print("")
    print("Area is {} mm².".format(math.pi * 15**2))
    print("Perimeter is {} mm².".format(2 * math.pi * 15))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
