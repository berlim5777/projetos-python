import random
numero1 = random.randint(1, 20)
numero2 = random.randint(1,20)
print("numero1:", numero1 )
print("numero2:", numero2)
if numero1 < numero2 :
    print("numero2:", numero2)
elif numero1 > numero2 :
    print("numero1:", numero1)
else:
    print("o numeros são iguais")