import random
from datetime import datetime
data = datetime.now()
nome = ["daniel", "miquel", "lucas", "magno", "caio"]
cidade = ["rio de janeiro", "belo horizonte", "espirtio santo"]
nome = random.choice(nome)
cidade = random.choice(cidade)
idade = random.randint(18, 60)
print("--Dados--")
print("nome: ", nome) 
print("idade: ", idade)
print("cidade: ", cidade)
print("horas: ", data.hour, ":", data.minute, ":", data.second)