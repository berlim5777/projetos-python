import random
preço_feijão = random.randint(1, 150)
if preço_feijão >=100:
    desconto = preço_feijão *10
    preço_final = desconto - preço_feijão
    print("preço com 10 porcento  de desconto", preço_final)
else:
    print("preço normal:", preço_feijão)