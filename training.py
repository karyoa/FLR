#!/usr/bin/env python2.7

import csv

theta0 = 0
theta1 = 0
tmptheta0 = 0
tmptheta1 = 0
sigma0 = 0
sigma1 = 0
m = -1
list = []

lr = -0.1

with open('data.csv') as f:
    readCSV = csv.reader(f)
    for row in readCSV:
        list.append(row)
        m += 1
j = 0
while j < 10:
    i = 1
    # tmptheta0 = theta0
    # tmptheta1 = theta1
    while i <= m:
        sigma0 = sigma0 + ((tmptheta0 + (tmptheta1 * int(list[i][0]))) - int(list[i][1]))
        sigma1 = sigma0 * int(list[i][0])
        i += 1
    # print (sigma0, sigma1)

    tmptheta0 = lr * (sigma0 / m)
    tmptheta1 = lr * (sigma1 / m)
    print (tmptheta0, tmptheta1)

    theta0 = theta0 - tmptheta0
    theta1 = theta1 - tmptheta1
    # print (theta0, theta1)
    j += 1
