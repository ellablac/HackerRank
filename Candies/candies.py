# !/bin/python3
# Program Name - candies.py
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

import math
import os
import random
import re
import sys

def candies(n, arr):
    """Given a list of students' ratings, return the number
    of candies"""

    forw = tally_up(arr)
    backw = tally_up(reversed(arr))
    backw.reverse()
    #the maximum values of each pair in 2 lists
    combined = [max(i) for i in zip(forw,backw)]
    TotalCandies = sum(combined)  
    
    return TotalCandies
        
def tally_up(arr):
    """Keep the running totals of the consecutive increases in
    a given sequence. """
    
    # For every non-increasing number, re-set the tally. 
    # The minimum score is 1. 
    
    ScoreCard = []
    prev = 0
    tally = 1
    for item in arr:
        if item > prev: # increasing
            ScoreCard.append(tally)
            tally +=1
        else: # non-increasing (less or equal)
            ScoreCard.append(1)
            prev = item
            tally = 2
        prev = item
            
    return ScoreCard

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
    # MainFromFile("C:/HackerRank/candies/in3.txt")
    HackerRankMain()