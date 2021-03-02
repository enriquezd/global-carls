'''
csv_combiner.py
February 2021

A python script to combine all CSV files in the same directory as this .py file, and create a new column that keeps track of the file name
from which a particular row came.

For best results, assure that all CSV's are of similar formatting.

Required Libraries: Pandas (https://pandas.pydata.org/)

'''

import pandas as pd
import glob, os

def main():

    cwd = os.getcwd()

    #Initializes a list of file paths that includes every csv file in the current working directory
    csvfiles = glob.glob(os.path.join(cwd, '*.csv'))

    dataframes = []
    for csv in csvfiles:
        base_file_name = os.path.basename(csv)
        file_name = os.path.splitext(base_file_name)[0]

        #Creates a dataframe copy of the csv file, with the file name appended as a column
        dataframe = pd.read_csv(csv)
        dataframe["Origin CSV"] = file_name
        dataframes.append(dataframe)

    combined_dataframe = pd.concat(dataframes, ignore_index=True)

    combined_dataframe.to_csv('combined_csv.csv')

if __name__ == '__main__':
    main()
