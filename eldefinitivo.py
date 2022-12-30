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


while True:

    puntosjuga=0
    puntoscom=0
    computer=['piedra', 'papel', 'tijera']
    user= input("objeto")
    user= user.lower()

    if not user in computer:
        print('no valido')
        continue

    
    computer= random.choice(computer)



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
    
    if puntosjuga == 3:
        print('SE ACABO GANO EL USER')
        break
    if puntoscom==3:
        print('SE ACABO GANO LA COMPU')
        break