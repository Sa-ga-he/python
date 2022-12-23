import random


'''''
matriz= [
    [1,4,7],
    [9,5,8],
    [6,3,9]
]

for variable1 in matriz:
    for variable2 in variable1:
        print(variable2)
'''''

puntosdetenerjuego=0
puntosjuga=0
puntoscom=0

while True:

    computer=['piedra', 'papel', 'tijera']

    computer= random.choice(computer)

    user= input("objeto")
    user= user.lower()

    if computer==user:
        print("empate")

    elif user=='piedra' and computer=='tijera':
        print('gana user')
        puntosjuga=+1
    
    elif user=='piedra' and computer=='papel':
        print('gana computer')
        puntoscom=+1
    
    elif user=='tijera' and computer=='papel':
        print('gana user')
        puntosjuga=+1
    
    elif user=='tijera' and computer=='piedra':
        print('gana computer')
        puntoscom=+1

    elif user=='papel' and computer=='piedra':
        print('gana user')
        puntosjuga=+1
    
    elif user=='papel' and computer=='tijera':
        print('gana computer')
        puntoscom=+1
    
    elif puntosjuga == 3:
        print('gana user')
        break
    elif puntoscom==3:
        print('gana computer')
        break