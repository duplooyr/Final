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