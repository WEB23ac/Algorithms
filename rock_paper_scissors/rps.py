#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    options = ('rock', 'paper', 'scissors')

    arr = [[] for i in range(0, 3**n)]

    def inner_recursion(n, sub_arr):
        for i in range(0, len(options)-1):
            sub_arr[i] = options[i]
        return sub_arr

# * looping through primary array which has 3^n length
    for i in range(0, 3**n):
      # * Inside of *that* array, we need to add possible moves to a list n long
        arr[i] = inner_recursion(n, arr[i])

    print(arr)
    pass


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
