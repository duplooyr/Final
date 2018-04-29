#!/usr/bin/env python
import plotly
import plotly.graph_objs as go
import sys

#file_open = raw_input("What CSV file would you like to open? ") + ".csv"
file_open = ("Businesses.csv")
data = open(file_open, 'r')
lines = data.readlines()

col_data = []
for row_count in range(0, len(lines)):
    info = lines[row_count].rstrip().split(",")
    col_data += [info]

row_len = len(lines)
first_row = col_data[[0][0]]


    
    
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
    x = raw_input("> ")
    if x == "1":
        escape()
        search_functions()
    elif x == "2":
        escape()
        sort_functions()
    elif x == "3":
        escape()
        graph_functions()
    elif x == "4":
        new = str(col_data)
        new = new.rstrip().split(",")
        print new 
        finished_prompt()
    elif x.lower == "exit" or x == "exit":
        sys.exit()
    elif x != "1" or "2" or "3" or "4" or "exit":
        main()
    elif x.isalpha() or len(x) > 1:
        main()

#//////////////////////////////////////////////////////////////////////////////////////////////// 
#                                       CHOICES
#//////////////////////////////////////////////////////////////////////////////////////////////// 

def choices(i):
    print bcolors.HEADER + bcolors.BOLD + "Record found which information would you like?" + bcolors.ENDC
    print bcolors.BOLD + "1) All"
    print "2) First Name"
    print "3) Last Name"
    print "4) Email"
    print "5) Department"
    print "6) Annual Income" + bcolors.ENDC
    choice = input("> ")
    if choice == 1:
        print bcolors.HEADER + bcolors.BOLD + id_number[i] + bcolors.ENDC + bcolors.BOLD, first_name[i], last_name[i], email[i], department[i], annual_income[i] + bcolors.ENDC
    elif choice == 2:
        print bcolors.BOLD + first_name[i] + bcolors.ENDC
    elif choice == 3:
        print bcolors.BOLD + last_name[i] + bcolors.ENDC
    elif choice == 4:
        print bcolors.BOLD + email[i] + bcolors.ENDC
    elif choice == 5:
        print bcolors.BOLD + department[i] + bcolors.ENDC
    elif choice == 6:
        print bcolors.BOLD + annual_income[i] + bcolors.ENDC
    else:
        escape()
        choices(i)

def choices_searches():
    print bcolors.HEADER + bcolors.BOLD + "What column would you like to search for?" + bcolors.ENDC

def beginning_choices():
    print bcolors.HEADER + bcolors.BOLD + "Welcome, which function would you like to use?" + bcolors.ENDC
    print bcolors.BOLD + "1) Search Data"
    print "2) Sort Data"
    print "3) Graph Data"
    print "4) Print Data" + bcolors.ENDC
def sort_choices():
    print bcolors.HEADER + bcolors.BOLD + "How would you like to sort the data?"  + bcolors.ENDC
    print bcolors.BOLD + "1) ID High to Low"
    print "2) Alphabetical First Name"
    print "3) Alphabetical Last Name"
    print "4) Income High to Low"
    print "5) Income Low to High" + bcolors.ENDC
def graph_choices():
    print bcolors.HEADER + bcolors.BOLD + "How would you like to graph your data?"  + bcolors.ENDC
    print bcolors.BOLD + "1) Income high to low with department"
    print "2) Income low to high with department" + bcolors.ENDC

#////////////////////////////////////////////////////////////////////////////////////////////////       
#                                           PROMPTS
#//////////////////////////////////////////////////////////////////////////////////////////////// 

#FINISHED PROMPT
def finished_prompt():
    print bcolors.HEADER + bcolors.BOLD +"\n\nDo you have everything you need? (Y/N)" + bcolors.ENDC
    x = raw_input(bcolors.FAIL + "> " + bcolors.ENDC).title()
    if x == "N":
        main()
    else:
        sys.exit()

#////////////////////////////////////////////////////////////////////////////////////////////////  
#                                       SEARCH FUNCTIONS
#//////////////////////////////////////////////////////////////////////////////////////////////// 

def search_f(inputed):
    row_number = input("Row #? ")
    found_row = col_data[row_number]
    print ("\n") 
    print bcolors.BOLD + found_row[inputed] + bcolors.ENDC
    finished_prompt()

#////////////////////////////////////////////////////////////////////////////////////////////////
#                                   FUNCTIONS
#////////////////////////////////////////////////////////////////////////////////////////////////      

def search_functions():
    print bcolors.BOLD + bcolors.HEADER + ("Would you like all data or one column?") + bcolors.ENDC
    print bcolors.BOLD + ("1.) One Column") + bcolors.ENDC
    print bcolors.BOLD + ("2.) All Data") + bcolors.ENDC

    inputed = input("> ")

    if inputed == 1:
        choices_searches()
        inputed = input("> ")

        if inputed <= len(first_row): 
            column_name = first_row[inputed]
            print ("You wish to search for %s?") % column_name
            y_n = raw_input("(Y/N)? ").lower()

            if y_n == "y":
                search_f(inputed)

            elif y_n == "n":
                search_functions()
            
            else:
                fail_option()
                search_functions()
        else:
            fail_option()
            search_functions()
    else:
        fail_option()
        search_functions()

def sort_functions():
    sort_choices()
    x = input("> ")
    if x == 1:
        id_h_l()
    elif x == 2:
        alp_first()
    elif x == 3:
        alp_last()
    elif x == 4:
        inc_h_l()
    elif x == 5:
        inc_l_h()
    else:
        escape()
        sort_functions()

def graph_functions():
    graph_choices()
    x = input("> ")
    if x == 1:
        g_1()
    elif x == 2:
        g_2()
    finished_prompt()

#////////////////////////////////////////////////////////////////////////////////////////////////      
#                                 SORT OPTIONS
#////////////////////////////////////////////////////////////////////////////////////////////////      

def id_h_l():
    n_ids = id_number[::-1]
    n_f = first_name[::-1]
    n_l = last_name[::-1]
    n_e = email[::-1]
    n_d = department[::-1]
    n_a = annual_income[::-1]
    for i in range(0,len(n_ids)):
        print bcolors.OKGREEN + n_ids[i] + bcolors.ENDC, bcolors.BOLD + n_f[i], n_l[i], n_e[i], n_d[i], n_a[i] + bcolors.ENDC
    finished_prompt()


def alp_first():
    new_list = first_name
    new_list.sort()
    for i in range(0,len(first_name)):
        print bcolors.OKGREEN + new_list[i] + bcolors.ENDC
    finished_prompt()


def alp_last():
    new_list = last_name
    new_list.sort()
    for i in range(0,len(last_name)):
        print bcolors.OKGREEN + new_list[i] + bcolors.ENDC
    finished_prompt()

def inc_h_l():
    x = annual_income
    x = map(float,x)
    x.sort(reverse=True)
    for i in range(0,len(annual_income)):
        print bcolors.BOLD + str(x[i]) + bcolors.ENDC
    finished_prompt()

def inc_l_h():
    x = annual_income
    x = map(float,x)
    x.sort()
    for i in range(0,len(annual_income)):
        print bcolors.BOLD + str(x[i]) + bcolors.ENDC
    finished_prompt()

#////////////////////////////////////////////////////////////////////////////////////////////////  
#                                   GRAPH TYPES
#////////////////////////////////////////////////////////////////////////////////////////////////      

def g_1():
    graph_store_type = department
    graph_income = annual_income
    
    graph_store_type = map(str, graph_store_type)
    graph_store_type.sort()

    graph_income = map(float,graph_income)
    graph_income.sort(reverse=True)


    data = [go.Bar(
        x = graph_store_type,
        y = graph_income
    )]
    plotly.offline.plot(data, filename='graph.html')

def g_2():
    graph_store_type = department
    graph_income = annual_income
    
    graph_store_type = map(str, graph_store_type)
    graph_store_type.sort(reverse=True)

    graph_income = map(float,graph_income)
    graph_income.sort()


    data = [go.Bar(
        x = graph_store_type,
        y = graph_income
    )]
    plotly.offline.plot(data, filename='graph.html')

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