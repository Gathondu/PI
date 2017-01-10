import math
import os
import sys

from decimal import Decimal


PI = math.pi
# find absolute value as exception returns a negative number
MAX_DECIMAL_PLACES = abs(Decimal(str(PI)).as_tuple().exponent)


def _clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# def _exit():
#     sys.exit(1)
#
#
# def quit():
#     # prompt for another run or an exit
#     if input("Do you want to Continue? [Y]es / [N]o: ") in ('y', 'Y', ''):
#         getPi()
#     else:
#         _exit()


def checkString(n):
    """This method ensures that the input by the user
    is not a string

    args: Takes in a value n which contains value to be tested

    returns: This method returns True if value is a string and raises
            a ValueError.
    """
    try:
        int(n)
    except ValueError as v:
        _clear()
        print("Input value must a number")
        return True


def checkLength(n):
    """This method ensures that the length described by the input
    is not longer than the number of decimal places in math.pi

    args: The length described by user input

    returns: This method returns True if length is longer than the number
    of decimal places
    """

    if round(n) not in range(0, MAX_DECIMAL_PLACES + 1):
        _clear()
        print("The number must be between 0 and {}"
              .format(MAX_DECIMAL_PLACES))
        return True


def getInput(n=None):
    # prompt the user for a number
    n = n or input("Enter the number of decimal"
                   " places between 0 and {}: "
                   .format(MAX_DECIMAL_PLACES))
    # Ensure input isn't a string
    if checkString(n):
        n = getInput()

    # check that the given input isn't longer than the decimal places in PI
    if checkLength(float(n)):
        n = getInput()

    _clear()
    return n


def getPi(n=None):
    n = getInput(n) or getInput()
    # convert PI up to N decimal places as defined by the user
    # return converted PI back to the user. N is also rounded
    # to the nearest 10.
    decimalPlaces = round(PI, round(float(n)))
    return "PI to {} decimal places is: {}".format(n, decimalPlaces)


if __name__ == "__main__":
    print(getPi())
