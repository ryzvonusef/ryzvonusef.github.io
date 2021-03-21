import csv
import pandas as pd

bFileName = './book_file.csv'


bTitle = str(input("please enter book title:\n"))
bAuthor = str(input("please enter book author:\n"))
bISBN = str(input("please enter book ISBN:\n"))

with open(bFileName, mode='a') as csv_file:
    fieldnames = ['Title', 'Author', 'ISBN']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    if csv_file.tell() == 0:
        writer.writeheader()
    writer.writerow({'Title': bTitle,'Author': bAuthor, 'ISBN': bISBN})
    
with open(bFileName, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are \n{", ".join(row)}')
            line_count += 1
        print(f'Title: {row["Title"]}, Author: {row["Author"]}, ISBN: {row["ISBN"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')


