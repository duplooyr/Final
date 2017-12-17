#!/usr/bin/env python
import plotly
import plotly.graph_objs as go

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
#////////////////////////////////////////////////////////////////////////////////////////////////  
#MAIN FUNCTION
def main():
    print(chr(27) + "[2J")
    beginning_choices()
    x = input("> ")
    if x == 1:
        print(chr(27) + "[2J")
        search_functions()
    elif x == 2:
        print(chr(27) + "[2J")
        sort_functions()
    elif x == 3:
        print(chr(27) + "[2J")
        graph_functions()
        
    elif x == 4:
        for i in range (0,len(id_number)):
            print bcolors.OKGREEN + id_number[i] + bcolors.ENDC, bcolors.BOLD + first_name[i], last_name[i], email[i], department[i], annual_income[i] + bcolors.ENDC
        finished_prompt()

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

def choices_searches():
    print bcolors.HEADER + bcolors.BOLD + "Would you like to search by?" + bcolors.ENDC
    print bcolors.BOLD + "1) Search by ID"
    print "2) Search by First Name"
    print "3) Search by Last Name"
    print "4) Search by Email"
    print "5) Search by Department"
    print "6) Search by Annual Income" + bcolors.ENDC

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
# SEARCH ID
def search_id(i_id):
    inputed_id = str(i_id)
    for i in range(0, len(id_number)):
        if id_number[i] == inputed_id:
            choices(i)
    finished_prompt()
# SEARCH FIRST NAME
def search_fname(i_name):
    inputed_name = str(i_name)
    for i in range(0, len(first_name)):
        if first_name[i] == inputed_name:
            choices(i)
    finished_prompt()
# SEARCH LAST NAME
def search_lname(i_name):
    inputed_name = str(i_name)
    for i in range(0, len(last_name)):
        if last_name[i] == inputed_name:
            choices(i)
    finished_prompt()
# SEARCH EMAIL
def search_email(i_name):
    inputed_name = str(i_name)
    for i in range(0, len(email)):
        if email[i] == inputed_name:
            choices(i)
    finished_prompt()
# DEPARTMENT EMAIL
def search_department(i_name):
    inputed_name = str(i_name)
    for i in range(0, len(department)):
        if department[i] == inputed_name:
            choices(i)
    finished_prompt()
# INCOME EMAIL
def search_income(i_name):
    inputed_name = str(i_name)
    for i in range(0, len(annual_income)):
        if annual_income[i] == inputed_name:
            choices(i)
    finished_prompt()

#////////////////////////////////////////////////////////////////////////////////////////////////       
# ID PROMPT
def id_prompt():
    x = input(bcolors.HEADER + bcolors.BOLD +"Which ID would you like to search for? " + bcolors.ENDC)
    print(chr(27) + "[2J")
    search_id(x) 
# FIST NAME PROMPT
def first_name_prompt():
    x = raw_input(bcolors.HEADER + bcolors.BOLD +"Which first name would you like to search for? " + bcolors.ENDC).title()
    print(chr(27) + "[2J")
    search_fname(x) 
# LAST NAME PROMPT
def last_name_prompt():
    x = raw_input(bcolors.HEADER + bcolors.BOLD +"Which last name would you like to search for? " + bcolors.ENDC).title()
    print(chr(27) + "[2J")
    search_lname(x) 
# EMAIL PROMPT
def email_prompt():
    x = raw_input(bcolors.HEADER + bcolors.BOLD +"Which email would you like to search for? " + bcolors.ENDC)
    print(chr(27) + "[2J")
    search_email(x) 
# DEPARTMENT PROMPT
def department_prompt():
    x = raw_input(bcolors.HEADER + bcolors.BOLD +"Which department would you like to search for? " + bcolors.ENDC).title()
    print(chr(27) + "[2J")
    search_department(x) 
# INCOME PROMPT
def income_prompt():
    x = raw_input(bcolors.HEADER + bcolors.BOLD +"How much income would you like to search for? " + bcolors.ENDC)
    print(chr(27) + "[2J")
    search_income(x) 
def finished_prompt():
    print bcolors.HEADER + bcolors.BOLD +"\n\nDo you have everything you need? (Y/N)" + bcolors.ENDC
    x = raw_input(bcolors.FAIL + "> " + bcolors.ENDC).title()
    if x == "N":
        main()
#////////////////////////////////////////////////////////////////////////////////////////////////     
def search_functions():
    choices_searches()
    inputed = input("> ")
    if inputed == 1:
        id_prompt()
    elif inputed == 2:
        first_name_prompt()
    elif inputed == 3:
        last_name_prompt()
    elif inputed == 4:
        email_prompt()
    elif inputed == 5:
        department_prompt()
    elif inputed == 6:
        income_prompt()

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

def graph_functions():
    graph_choices()
    x = input("> ")
    if x == 1:
        g_1()
    elif x == 2:
        g_2()
    finished_prompt()
 
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