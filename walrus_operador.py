# walrus :=

# Atribui valores para variáveis em expressões maiores

comidas = list()

while comida := input("Que comida você gosta?: ") != "sair":
    comidas.append(comida)
