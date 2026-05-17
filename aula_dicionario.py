usuario = []

for i in range(3):
   pessoa={}
   pessoa["nome"] = input(" nome: ")
   pessoa["iddae"] = input(" idade: ")
   pessoa["cidade"] = input("cidade: ")
   usuario.append(pessoa)
print(usuario)