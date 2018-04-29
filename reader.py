#!/usr/bin/env python
import sys

print(chr(27) + "[2J")
file_open = raw_input("What CSV file would you like to open? ").rstrip() + ".csv"
#file_open = ("test1.csv")
data = open(file_open, 'r')
lines = data.readlines()
first = True
data_array = [[]]
for row_count in range(0, len(lines)):
    if first == True:
        first = False
    else:
        data_array.append([])
    info = lines[row_count].rstrip().split(",")
    
    for col_count in range(0, len(info)):
        data_array[row_count].append(info[col_count]) 
    

row_len = len(lines)
first_row = lines[0].rstrip().split(",")



    
    
#////////////////////////////////////////////////////////////////////////////////////////////////  
#                                        ABSTRACTED FUNCTIONS
#//////////////////////////////////////////////////////////////////////////////////////////////// 

def fail_option():
    escape()
    print ("\n")
    print bcolors.WARNING + ("Please pick a valid option.") + bcolors.ENDC
    print ("\n")

def escape():
    print(chr(27) + "[2J")

def main():
    escape()
    beginning_choices()
    x = raw_input("> ").rstrip()
    if x == "1":
        escape()
        search_functions()
    elif x == "2":
        print_data()
    elif x.lower == "exit":
        sys.exit()
    elif x != "1" or "2" or "exit":
        main()
    elif x.isalpha() or len(x) > 1:
        main()

#//////////////////////////////////////////////////////////////////////////////////////////////// 
#                                       CHOICES
#//////////////////////////////////////////////////////////////////////////////////////////////// 

def beginning_choices():
    print bcolors.HEADER + bcolors.BOLD + "Welcome, which function would you like to use?" + bcolors.ENDC
    print bcolors.BOLD + "1) Search Data"
    print "2) Print Data" + bcolors.ENDC
def finished_prompt():
    print bcolors.HEADER + bcolors.BOLD +"\n\nDo you have everything you need? (Y/N)" + bcolors.ENDC
    x = raw_input(bcolors.FAIL + "> " + bcolors.ENDC).title()
    if x == "N":
        main()
    else:
        sys.exit()

#////////////////////////////////////////////////////////////////////////////////////////////////  
#                                       FUNCTIONS
#//////////////////////////////////////////////////////////////////////////////////////////////// 

def search_f(inputed):
    print ("\n")
    print (bcolors.BOLD + "Search for..." + bcolors.ENDC)
    search_key = raw_input("> ").rstrip()
    for i in range(0,row_len):
        if search_key == data_array[i][inputed]:
            print data_array[i]
            finished_prompt()
        elif i == row_len-1 and data_array[i][inputed] != search_key:
            print ("\n") 
            print bcolors.WARNING + "No results found." + bcolors.ENDC
            print ("\n")
            search_f(inputed)

def search_functions():
    s_column_n = input(bcolors.BOLD + "What column # would you like to search by? " + "(0-%d) " % (len(info)-1) + bcolors.ENDC) 
    if s_column_n <= len(info)-1:
        column_name = first_row[s_column_n]
        print (bcolors.BOLD + "You wish to search by " + bcolors.HEADER + "%s?" + bcolors.ENDC) % column_name
        y_n = raw_input(bcolors.BOLD + bcolors.HEADER + "(Y/N)? " + bcolors.ENDC).lower().rstrip()
        if y_n == "y":
            search_f(s_column_n)
        elif y_n == "n":
            search_functions()
        elif y_n != "y" or "n":
            fail_option()
            search_functions()
    elif s_column_n > len(info)-1:
        fail_option()
        search_functions()

def print_data():
    escape()
    for x in range(0,row_len):
        row_val = ""
        for y in range(0,len(info)):
            row_val += data_array[x][y] + " "
        print bcolors.BOLD + row_val + bcolors.ENDC
    finished_prompt()    

#////////////////////////////////////////////////////////////////////////////////////////////////  
#                               TEXT COLORING
#////////////////////////////////////////////////////////////////////////////////////////////////      

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
main()