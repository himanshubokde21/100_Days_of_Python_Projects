import sys
import os

currDict = {}

with open('currenciesData.txt', 'r') as f:
  for line in f:
    parsed = line.split('\t')
    if len(parsed) >= 2:  
      currDict[parsed[0]] = parsed[1]
amt = float(input('Enter amount:'))
print('\nCurrencies: \n')
[print(item) for item in currDict.keys()]
currency = input('\nEnter currency: ')
print(f'{amt} INR => {amt*float(currDict[currency])} {currency}')
