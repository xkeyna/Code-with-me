#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 13:14:39 2022

@author: sakinahrosli
"""


# function for outer character and filled character
def in_diamond(ch, i, character, filled, fillCharacter):
    # total num of character in a row, if same, exit while loop
    while (ch != (2 * i - 1)):

        # position of outer character: ch == 0 first character, ch == 2 * i - 2 last character
        if (ch == 0 or ch == 2 * i - 2):
            print("{}".format(character), end="")

        # types of filled characters to use
        else:
            if (filled == True):
                print("{}".format(fillCharacter), end="")
            if (filled == False):
                print(" ", end="")

        # increase count of character by 1
        ch += 1

# main function
# set default fillCharacter='-', if not specified


def diamondPrinter(height, character, filled, fillCharacter='-'):
    # height of diamond minimum 3
    if height > 2:

        # separate the diamond into upper part and lower part based on height
        # middle row would be height divided with 2
        n = (height + 1)//2

        # string to be printed at the middle diamond
        string1 = 'Lancaster University!'

        # Upper diamond
        for i in range(1, n + 1):
            # rows before middle of diamond
            if (i != n):
                # Print spaces
                for space in range(1, n-i+1):
                    print(" ", end="")

                # set counter for number of character
                ch = 0
                # call function for character
                in_diamond(ch, i, character, filled, fillCharacter)
                # newline
                print()

            else:

                # middle diamond where i == n
                # calculate the number of filled characters needed
                mid_n = int((height - len(string1) - 2)/2)
                # specify the type of character to be used
                if (filled == True):
                    # print string1 based on height of diamond
                    # middle col == height of diamond
                    # -2 as we need to consider the outer cahracter
                    print("{}".format(character) +
                          "{}".format(fillCharacter) * mid_n +
                          string1[0:n*2-3] +
                          "{}".format(fillCharacter) * mid_n +
                          "{}".format(character))

                if (filled == False):
                    # if false, the filled characters are just empty space
                    print("{}".format(character) + ' ' * mid_n +
                          string1[0:n*2-3] +
                          " " * mid_n +
                          "{}".format(character))

        # reset n for lower diamond
        n = n - 1

        # Lower diamond
        # start n, stop 0, decrease by 1
        for i in range(n, 0, -1):
            # Print spaces (spaces increases as it reach bottom diamond)
            for space in range(0, n-i+1):
                print(" ", end="")

            # set counter for number of character
            ch = 0
            # call function for character
            in_diamond(ch, i, character, filled, fillCharacter)
            # newline
            print()
    else:
        print('Error')


diamondPrinter(5, '*', True, 'o')
diamondPrinter(7, '*', True, 'x')
diamondPrinter(25, '*', True)
diamondPrinter(29, '#', False)
diamondPrinter(4, 'a', False)
diamondPrinter(2, 'a', False)
diamondPrinter(-2, 'a', False)
diamondPrinter(27, 'x', True)
