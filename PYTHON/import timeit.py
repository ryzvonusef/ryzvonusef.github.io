import timeit
import csv
import pandas as pd

filename = './book_file.csv'

def talktime(filename, funcname, func):
    print(f"# {funcname}")
    t = timeit.timeit(f'{funcname}("{filename}")', setup=f'from __main__ import {funcname}', number = 100) / 100
    print('Elapsed time : ', t)
    print('n = ', func(filename))
    print('\n')

def sum1forline(filename):
    with open(filename) as f:
        return sum(1 for line in f)
talktime(filename, 'sum1forline', sum1forline)
