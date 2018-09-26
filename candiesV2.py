# !/bin/python3
# Program Name - candiesV2.py
# Written by - Ella Blackledge
# Date - 09/21/2018
#
# Problem Statement:
#
# Alice is a kindergarten teacher. She wants to give some candies to
# the children in her class.  All the children sit in a line and each
# of them has a rating score according to his or her performance
# in the class.  Alice wants to give at least 1 candy to each child.
# If two children sit next to each other, then the one 
# with the higher rating must get more candies. Alice wants to minimize
# the total number of candies she must buy.
#
# Example: 
# Students' ratings are [4, 6, 4, 5, 6, 2]. 
# She gives the students candy in the following  amounts: [1, 2, 1, 2, 3, 1]. 
# She must buy a minimum of 10 candies.
#
# Solution:
# If we require that any increasing subsequence {IS} followed
# by a decreasing subsequence {DS} must have size |IS| > |DS|,
# then this problem has a trivial solution.
# Consider this sequence: {4,5,6,7,7,5,4,3}.
# The corresponding candies sequence is {1,2,3,4,4,3,2,1}.
# Since we only need to return the sum of elements in the sequence,
# this is the valid alternative: {1,2,3,4,1,2,3,4}, and it that can be found
# in a single pass.
# 
# This approach does not work when an increasing sequence is followed by
# a decreasing sequence of a larger size: for a sequence {4,5,6,7,5,4,3,2,1} 
# the candies array is {1,2,3,6,5,4,3,2,1} . We can use the
# technique above, but 4 (the last candy element of the increasing sequence)
# must be reaplaced by 6. The solution is to add 4, and later compensate
# for the shortage by adding 2 (6-4).

import math
import os
import random
import re
import sys


def candies(n, arr):
    """Given a list of students' ratings, return the number
    of candies"""

    # the accumulator for the total number of candies
    TotalCandies = 0
    # candies counter for each element
    candies = 1
    # number of elements in the last encountered increasing sequence
    saved_cand = 1
    direc = "UP"
    prev_dir = "DOWN"

    for i in range (1, n):

        direc = direction(arr[i-1], arr[i])
        # end of the decreasing subsequence
        if prev_dir == "DOWN" and direc != "DOWN":
            TotalCandies += max (0, candies - saved_cand + 1)
            saved_cand = 1

        if direc == "FLAT":
            candies = 1
            saved_cand = 1

        elif direc == prev_dir:
            candies += 1

        elif direc == "UP": # start of a new increasing subsequence
                candies = 2

        else: # dir == "DOWN" start of a new decreasing subsequence
            saved_cand = candies # saved the size of the previous subsequence
            candies = 1

        TotalCandies += candies
        prev_dir = direc

    if prev_dir == "DOWN":
            TotalCandies += max (0, candies - saved_cand + 1)
  
    return TotalCandies

def direction (old, curr):
    if old > curr:
        return "DOWN"
    elif old < curr:
        return "UP"
    else:
        return "FLAT"
        

def MainFromFile(fname):
    # read input from from file and print to stdout
    f = open (fname, "r")
    n = int(f.readline())
    arr = []

    for _ in range(n):
        arr_item = int(f.readline())
        arr.append(arr_item)
    
    result = candies(n, arr)

    print(str(result) + '\n')

    f.close()

def HackerRankMain():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

if __name__ == '__main__':
    # One of the two lines below must be commented out
    MainFromFile("C:/HackerRank/candies/input01.txt")
    #HackerRankMain()