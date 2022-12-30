'''''
set_countryes = {'COLOMBIA', 'MEX', 'BOL'}

set_countryes.add('esp')
print(set_countryes)


#number=[elem*2 for elem in range(1,105) if elem%2==0]
#print(number)

import random

countri= ['col', 'per', 'espa']
popu= {}
for country in countri:
    popu[country]=random.randint(1,100)

print(popu)


num1= [2,5,7,9]
num2= [5,76,8,9,0]

result= num1+num2

print(result)
'''''

import sys

print(sys.path)