#!/usr/bin/env python2.7

import csv
from utils import sigmatheta0, sigmatheta1, estimate_price

theta0 = 0.0
theta1 = 0.0
tmptheta0 = 0.0
tmptheta1 = 0.0
learningrate = 0.0001
price = []
mileage = []

with open('data.csv') as f:
	read = csv.reader(f)
	for r in read:
		if r[0].isdigit():
			mileage.append(r[0])
		if r[1].isdigit():
			price.append(r[1])

mileage = map(float, mileage)
price = map(float, price)

m = len(mileage)
for i in range(0, m):
	mileage[i] /= 1000

for i in range(0, m):
	price[i] /= 1000

# for i in range(0, m):
# 	print (i, mileage[i])

while True:
	pretheta0 = theta0
	pretheta1 = theta1

	tmptheta0 = (learningrate * (sigmatheta0(theta0, theta1, mileage, price, m) / float(m)))
	tmptheta1 = (learningrate * (sigmatheta1(theta0, theta1, mileage, price, m) / float(m)))

	theta0 -= tmptheta0
	theta1 -= tmptheta1
	print (theta0, theta1)
	# print (tmptheta0, tmptheta1)
	if (pretheta0 == theta0 and pretheta1 == theta1):
		break
