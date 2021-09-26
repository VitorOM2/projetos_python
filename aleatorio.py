import random

# ===== VARIÁVEIS =====

dado    = random.randint (1,6)          # ** randint() numero inteiro aleatório **
x       = random.random  ()             # ** número aleatório entre 0 e 1      **
jokenpo = ['pedra', 'papel', 'tesoura']
z       = random.choice (jokenpo)       # ** eschole um item aleatório de uma lista **
cartas  = [1,2,3,4,5,6,7,8,9,'J','Q','K','A']
random.shuffle(cartas)

# ===== VARIÁVEIS =====

# ===== EXIBIR =====

print ( 'Dado: {}'.format(dado) )
print (x)
print ( 'Jokenpô: {}'.format(z) )
print ( cartas )

# ===== EXIBIR =====