print("=== TO DO LIST ===")
tarefas = []
def carregar_tarefas():
    try:
        arquivo = open("tarefas", "r")
        for linha in arquivo:
            tarefa.append(linha.strip())
        arquivo.close()
    except:
        pass
def salvar_tarefas():
    arquivo = open("tarefas.txt", "w")
    for tarefa in tarefas:
        arquivo.write (tarefa + "\n")
    arquivo.close()
carregar_tarefas()
while True:
    print("\n1 - Ver tarefas")
    print("2 - Adicionar tarefa")
    print("3 - Remover tarefa")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        print("\ntarefas")
        for i, tarefa in enumerate(tarefas, start=1):
            print(i, "-", tarefa)

    elif opcao == "2":
        tarefa = input("Digite a nova tarefa: ")
        tarefas.append(tarefa)
        salvar_tarefas()
        print("Tarefa adicionada!")

    elif opcao == "3":
        try:
            numero = int(input("qual tarefa quer remover: "))
            tarefas.pop(numero - 1)
            salvar_tarefas()
            print(" removida ")
        except:
            print("numero invalido")

    elif opcao == "4":
        print("Saindo...")
        break