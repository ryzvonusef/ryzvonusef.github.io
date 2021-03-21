import csv
import pandas as pd

bFileName = './book_file_1.csv'

cFileName = './book_file_2.csv'

eFileName = './employee_file.csv'


def bWriter(a,b,c,d):
    with open(bFileName, mode='a', newline='') as csv_file:
        fieldnames = ['Title','Author','ISBN','Lent']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        if csv_file.tell() == 0:
            writer.writeheader()
        writer.writerow({'Title':a,'Author':b, 'ISBN':c, 'Lent':d})


def bReader():
    df1 = pd.read_csv(bFileName)
    print (df1)
    
def bInput():
    bTitle = str(input("please enter book title:\n"))
    bAuthor = str(input("please enter book author:\n"))
    bISBN = int(input("please enter book ISBN:\n"))
    bLent = "0"
    
    
    bWriter(bTitle,bAuthor,bISBN,bLent)

#bInput()

#bReader()

#df = df.dropna(axis=0)


#df.insert(0, 'row_num', range(0,len(df)))  # here you insert the row count

'''
def bCheck():
    df1 = pd.read_csv(bFileName)
    rxw = int(input("enter ISBN Number of Book:\n"))
    rxv = df1[df1['ISBN']==rxw].index[0]

    if df1['Lent'][rxv] == 0:
        print (df1['Title'][rxv] + " is Available")
    else:
        print ("Not available")

bCheck()
'''
def bLender():
    df1 = pd.read_csv(bFileName)
    df2 = pd.read_csv(cFileName)
    df3 = pd.read_csv(eFileName)
    #print(df1)
    #print(df2)
    #print(df3)
    rxw = int(input("enter ISBN Number of Book:\n"))
    exw = int(input("enter E-ID:\n"))
    #rxv = df1[df1['ISBN']==rxw].index[0]
    #df1.loc[rxv,'Lent']=1
    #df1.to_csv(bFileName, index = False)

    cond1 = df1.ISBN == rxw
    cond2 = df3[df3['Emp_ID']==exw].index[0]
    rows1 = df1.loc[cond1, :]
    rows2 = df3.loc[cond2,'FirstName']
    df2 = df2.append(rows1, ignore_index=True)
    df2.E_ID.iloc[-1] = rows2
    #df1.drop(rows1.index, inplace=True)
    
    #df1.to_csv(bFileName, index = False)
    df2.to_csv(cFileName, index = False)

bLender()    



'''

def bLender():
    df1 = pd.read_csv(bFileName)
    rxw = int(input("enter ISBN Number of Book:\n"))
    rxv = df1[df1['ISBN']==rxw].index[0]
    df1.loc[rxv,'Lent']=1
    df1.to_csv(bFileName, index = False)

bLender() 

'''


"""
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
"""
