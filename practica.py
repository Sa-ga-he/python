import random

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
        

    elif user=='tijera':
        if computer=='papel':
            print('gana user')
            puntosjuga=+1
        else:
            print('gana computer')
            puntoscom=+1
    
    elif user=='papel':
        if computer=='piedra':
            print('gana user')
            puntosjuga=+1
        else:
            print('gana computer')
            puntoscom=+1
    
    elif user=='piedra':
        if computer=='tijera':
            print('gana user')
            puntosjuga=+1
        else:
            print('gana computer')
            puntoscom=+1




    if puntosjuga == 3:
        print('gana user')
        break
    elif puntoscom==3:
        print('gana computer')
        break