import csv
import os

File1 = 'zoobooks.csv'
File2 = 'zoobooks_cleaned.csv'

with open(File1, "r") as csv_file, open(File2, "w") as cleaned_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    cleaned_writer = csv.writer(cleaned_file, delimiter=';')

    for row in csv_reader:
        for column in row:
            cleaned_writer.writerow([column])





        