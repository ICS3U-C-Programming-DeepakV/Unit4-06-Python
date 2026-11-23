#!/usr/bin/envpython3
# Created By:Deepak
# Date: 11/02/2026
# This program is a loop that generates random numbers for you to guess
def main():

    for red in range(0, 3):
        for green in range(0, 3):
            for blue in range(0, 3):
                print(f"RGB: ({red}, {green}, {blue})")


if __name__ == "__main__":
    main()
