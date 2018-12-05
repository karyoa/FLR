#!/usr/bin/env python2.7

def	estimate_price(theta0, theta1, mileage):
	return (theta0 + (theta1 * mileage))

def	sigmatheta0(theta0, theta1, mileage, price, m):
	res = 0.0
	for i in range(0, m):
		res += estimate_price(theta0, theta1, mileage[i]) - price[i]
	return (res)

def	sigmatheta1(theta0, theta1, mileage, price, m):
	res = 0.0
	for i in range(0, m):
		res += (estimate_price(theta0, theta1, mileage[i]) - price[i]) * mileage[i]
	return (res)
