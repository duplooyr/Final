#!/usr/bin/env python
import sys
from collections import Counter

data = open("Businesses.csv", 'r')
lines = data.readlines()

id_number = []
first_name = []
last_name = []
email = []
department = []
annual_income = []
for i in range(1, len(lines)):
    info = lines[i].rstrip().split(",")
    id_number.append(info[0])
    first_name.append(info[1])
    last_name.append(info[2])
    email.append(info[3])
    department.append(info[4])
    annual_income.append(info[5])


def choices(i):
    print "Record found which information would you like?"
    print "1) All"
    print "2) First Name"
    print "3) Last Name"
    print "4) Email"
    print "5) Department"
    print "6) Annual Income"
    choice = input("> ")
    if choice == 1:
        print id_number[i], first_name[i], last_name[i], email[i], department[i], annual_income[i]
    elif choice == 2:
        print first_name[i]
    elif choice == 3:
        print last_name[i]
    elif choice == 4:
        print email[i]
    elif choice == 5:
        print department[i]
    elif choice == 6:
        print annual_income[i]


# SEARCH ID
def search_id(i_id):
    inputed_id = str(i_id)
    
    for i in range(0, len(id_number)):
        if id_number[i] == inputed_id:
            choices(i)

            
# PROMPT
def prompt():
    x = input("Which ID would you like to search for? ")
    print(chr(27) + "[2J")
    search_id(x) 


#MAIN FUNCTION
def main():
    print "Welcome which function would you like to use?"
    if raw_input("> ").lower() == "search_id":
        prompt(id)


main()