import random
letras = "abcdefghijklmnopqrstuvwxyz"
numeros = "123456789"
simbolos = "!@#$%¨&*"
tamanho = int(input("qual o tamnho da sua senha: "))
senhas = ""
todos = letras + numeros + simbolos
for i in range(tamanho):
    senhas +=  random.choice(todos)
    print("senha gerada: ", senhas)