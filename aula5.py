import random
numero_secreto = random.randint(1, 10)
chute = int(input("adivinhe o numero: "))
if chute == numero_secreto:
    print("acerto!!")
else:
    print("errou o numero secreto era", numero_secreto)