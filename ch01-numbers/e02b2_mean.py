#!/usr/bin/env python3
"""Solution to chapter 1, exercise 2, beyond 2: mean"""


def mean(numbers):
    """Accepts a non-empty list of numbers.

Returns the mean of those numbers.
"""
    return sum(numbers) / len(numbers)


def running():
    tn = []
    for i in range(4):
        n = float(input('Enter your 10 Running time score: '))
        print(f'{i+1}st Running time {n}')
        tn.append(n)
    print(f'Running monthly mean time {mean(tn):.2f} over {len(tn)} days') 


running()