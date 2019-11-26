"""Puzzle.

Usage:
  puzzle.py
  puzzle.py -h
  puzzle.py -t

Options:
  -h --help             Show this screen.
  -t --noterminal       Do not open terminal
"""

from docopt import docopt
from random import randint
import os

def to_bin(n):
    b = bin(n)[2:]
    return (5 - len(b)) * "0" + b

if __name__== "__main__":
    args = docopt(__doc__)
    if not args["--noterminal"]:
        os.system('gnome-terminal -x sh -c "python3 puzzle.py -t; bash"')
        exit(0)
    psw = "message"
    n = 3
    l = len(psw)

    print("Enter 0 for x and y to attempt a solution")
    while True:
        try:
            x = int(input("Enter number x: "))
            y = int(input("Enter number y: "))
        except ValueError:
            print("ERROR: you must enter a number!")
            continue
        if x == 0 and y == 0:
            attempt = str(input('Enter password: '))
            if attempt == psw:
                print("Success")
                break
        if x > 3 or x <= 0:
            print("error: invalid x")
            continue
        if y > l or y <= 0:
            print("error: invalid x")
            continue
        msg = ""
        for i in range(n):
            if i == x - 1:
                s = psw[y-1]
                m = ord(s) - ord('a') + 1
                msg += to_bin(m) + " "
            else:
                msg += to_bin(randint(1,26)) + " "
        print(msg)
