# list comprehension =  uma forma de criar listas com menos sintaxes
#                       pode imitar certas funções lambda e é mais facil de ler
#                       list = [expressão for item in iterable]
#                       list = [expressão for item in iterable if condicional]
#                       list = [expressão if/else for item in iterable]

# ===== Exemplo 1 =====
# ===== Sem list comprehension =====
ao_quadrado = []                # cria uma lista vazia
for i in range(1,11):           # cria um for loop
    ao_quadrado.append(i * i)   # define o que cada loop vai fazer
print(ao_quadrado)

# ===== Com list comprehension =====
# cria uma lista e define o que cada loop vai fazer
ao_quadrado = [i * i for i in range(1,11)]
print(ao_quadrado)

# ===== Exemplo 2 =====
# ===== Sem list comprehension =====
alunos = [100, 90, 80, 70, 60, 50, 40, 30, 0]
#alunos_aprovados = list( filter (lambda x: x >= 60, alunos) )

# ===== Com list comprehension =====
# alunos_aprovados = [i for i in alunos if i >= 60]
alunos_aprovados = [i if i >= 60 else "Reprovado" for i in alunos]

print (alunos_aprovados)