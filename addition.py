#!/usr/bin/env python3

# Created by Ethan Prieur
# Created on March 2022
# This is a program that does addition with two given numbers


def main():
    # This Function does the math

    # Input
    one = int(input("Enter Number One: "))
    two = int(input("Enter Number Two: "))

    # Process
    total = one + two

    # Output
    print("{0} + {1} = {2}".format(one, two, total))

    print("\nDone")


if __name__ == "__main__":
    main()
