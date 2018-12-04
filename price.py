#!/usr/bin/env python2.7

import csv

theta0 = 0
theta1 = 0
with open('theta.csv') as f:
    readCSV = csv.reader(f)
    for row in readCSV:
        tmp1 = row[0]
        tmp2 = row[1]
theta0 = float(tmp1)
theta1 = float(tmp2)
km = 0
km = input('Entrer le kilometrage du vehicule: ')
price = 0
price = theta0 + (theta1 * float(km))
print (price)
