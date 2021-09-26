# *** Sort() Método: Apenas para listas.
# *** Sort() Função: Usados para iterables.

# ===== EXEMPLO 1 =====
# alunos = ('João', 'Maria', 'Fernando', 'Mariane')
# alunos_alfabetica = sorted(alunos)

# alunos.sort() # Apenas listas []

# for i in alunos_alfabetica:
#     print (i)

# ===== EXEMPLO 2 =====

alunos = [
    ('João', 'F', 50),
    ('Maria', 'D',60),
    ('Fernando', 'A', 100),
    ('Mariane', 'B', 90)
]

nota = lambda notas : notas[1] # Coloca em ordem alfábetica pelo segundo item
alunos.sort(key= nota)

for i in alunos:
    print (i)