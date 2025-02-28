# PUA, Charles Michael G.
# TW23

import csv
#declare as dictionary 
exRates ={} 

with open("currency.csv", mode="r") as file:
    reader = csv.reader(file)
    next(reader) 
    for row in reader:
        code, name, rate = row
        exRates[code] = float(rate)
        
dollar = float(input("Enter the amount in dollars: "))
currency = input("Enter the currency code: ").upper()

if currency in exRates:
    convertedMoney = dollar * exRates[currency]
    print(f"\nDollar: {dollar} USD")
    print(f"{currency}: {convertedMoney:.9f}")
else:
    print("Currency not found")