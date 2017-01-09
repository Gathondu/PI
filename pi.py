import math
import os
import sys

from decimal import Decimal


PI = math.pi
# find absolute value as exception returns a negative number
MAX_DECIMAL_PLACES = abs(Decimal(str(PI)).as_tuple().exponent)


def _clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def _exit():
    sys.exit(1)


def getInput():
    # prompt the user for a number
    n = int(input("Enter the number of decimal places between 0 and {}: "
                  .format(MAX_DECIMAL_PLACES)))
    # check that the given input isn't longer than the decimal places in PI
    if n not in range(0, MAX_DECIMAL_PLACES + 1):
        _clear()
        print("The number must be between 0 and {}"
              .format(MAX_DECIMAL_PLACES))
        n = getInput()
    _clear()
    return n


def getPi():
    n = getInput()
    # convert PI up to N decimal places as defined by the user
    # return converted PI back to the user
    decimalPlaces = float("{0:.{1}f}".format(PI, n))
    print("PI to {} decimal places is: {}".format(n, decimalPlaces))

    # prompt for another run or an exit
    if input("Do you want to Quit? [Y]es / [N]o: ") in ('y', 'Y', ''):
        _exit()
    else:
        getPi()

if __name__ == "__main__":
    getPi()
