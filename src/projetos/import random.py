import random
conta = input("qual seu nome? ")
arquivo = open("id_contas.txt", "r")
lg = arquivo.readlines()
for linha in lg:
    if conta in linha:
      print("vc ja esta cadastrado") 
      break
else:
    print("cadastro feito ") 

    arquivo = open("id_contas.txt", "a")
    saldo = random.randint(1,1000)
    arquivo.write("\nnome:" + conta +"  " +  "saldo:" + str(saldo))
    print("conta já existe")
    arquivo = open("id_contas.txt", "r")
    arquivo.close()

while True:
    print("===serviços===")
    print("\n1-ver saldo")
    print("2-fazer saque")
    print("3-Fazer de1posito")
    op = input("qual sua escolha:")

    if op == "1":

        arquivo = open("id_contas.txt", "r")
        nome = input("qual seu nome? ")
        linhas = arquivo.readlines()
        for linha in linhas:
             if nome in linha:
                print(linha)
        arquivo.close()
               

    elif op == "2":
        arquivo = open("id_contas.txt", "r")
        nome1 = input("qual seu nome? ")
        linhas1 = arquivo.readlines()
        for linha in linhas1:
            if nome1 in linha:
                partes = linha.split("saldo:")
                saldo = int(partes[1])
                print(linha)
        saque = int(input("qual o valor do seu saque? "))
        if saque <= saldo:
            print("saque realizado")
            sd = saldo - saque
            novas_linhas = []
            for linha in linhas1:
                if nome1 in linha:
                    novas_linhas.append("\nnome:" + nome1 + "  saldo:" + str(sd))
                else:
                    novas_linhas.append(linha)
            arquivo = open("id_contas.txt", "w")
            arquivo.writelines(novas_linhas)
            print("seu saldo atual: ", sd)
        else:
             print("saldo insuficiente")   
        arquivo.close()  
    elif op == "3":
        arquivo = open("id_contas.txt", "r")
        nome2 = input("qual seu nome? ")
        
        linhas2 = arquivo.readlines()
        novas_linhas = []
        for linha in linhas2:
            if nome2 in linha:
                partes = linha.split("saldo:")
                saldo = int(partes[1])
                deposito = int(input("qual o valor do deposito? "))
                dp = deposito + saldo
                print("seu saldo atual: ", dp)
                print("deposito feito com sucesso")
                novas_linhas.append("\nnome:" + nome2 + "  saldo:" + str(dp))
                print(linha)
                
            else:
                    novas_linhas.append(linha)
        arquivo = open("id_contas.txt", "w")
        arquivo.writelines(novas_linhas)
        
        
        
        arquivo.close()   
arquivo = open("id_contas.txt", "r")
arquivo.close()