# *** While loop é uma instrução para executar uma parte do código enquanto a condição for verdadeira ***

# ----- VARIÁVEIS -----
nome = None
# ----- VARIÁVEIS -----

# ----- While Loop -----
while not nome:
    nome = str ( input ( "Escreva o seu nome: " ) )
# ----- While Loop -----

print ( "Olá " + nome )