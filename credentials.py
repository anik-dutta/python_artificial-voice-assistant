import csv
from mainframe import *

def register(name, email, password, city, number):
    with open('account.csv', mode='r+', newline='') as csvFile:        
        fileReader = csv.reader(csvFile)
        for row in fileReader:
            if row[0] == name:
                return 'false'

        fileWriter=csv.writer(csvFile)
        fileWriter.writerow([name, password, email, city, number])
        return 'true'

def login(name, password):
    with open('account.csv', 'r') as csvFile:
        fileReader = csv.reader(csvFile)
        for row in fileReader:
            if row[0] == name and row[1] == password:
                set_current_user(row[0])
                return '0'
            elif row[0]==name and row[1]!=password:
                return '1'
        return '2'