'''
add_spaces.py
February 2021

A python script to iterate through every cell in a given column of strings in a csv file, replacing the string with a version such that
every capital letter -- with the expection of the first -- has a space before it. (i.e, 'GlobalCarls' would become 'Global Carls')

Usage: input a csv file name and the name of the column in the csv you'd like to add spaces to. (Order specific)
E.g: python3 add_spaces.py my_file.csv column


Required Libraries: Pandas (https://pandas.pydata.org/)

'''

import pandas as pd
import re, sys

'''
A regex substitution function to implement the described string transformation.

Input: a string (preferably of the form 'WordWordWord')
Output: The same string but with spaces added before every capital letter (i.e, 'Word Word Word')
'''
def add_spaces(string):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", string)

def main():

    file = sys.argv[1]
    column = sys.argv[2]

    dataframe = pd.read_csv(file)

    dataframe[column] =  [re.sub(r"(\w)([A-Z])", r"\1 \2", str(row)) for row in dataframe[column]]

    dataframe.to_csv("file_with_spaces.csv")

if __name__ == '__main__':
    main()
