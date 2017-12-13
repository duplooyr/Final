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
# SEARCH ID
def search_fname(i_name):
    inputed_name = str(i_name)
    for i in range(0, len(first_name)):
        if first_name[i] == inputed_name:
            choices(i)

            
# ID PROMPT
def id_prompt():
    x = input("Which ID would you like to search for? ")
    print(chr(27) + "[2J")
    search_id(x) 
# FIST NAME PROMPT
def first_name_prompt():
    x = input("Which first name would you like to search for? ")
    print(chr(27) + "[2J")
    search_fname(x) 


#MAIN FUNCTION
def main():
    print "Welcome which function would you like to use?"
    inputed = raw_input("> ").lower()
    if inputed == "search_id":
        id_prompt()
    elif inputed == "search_fname":
        first_name_prompt()

main()