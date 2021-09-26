# *** Uma parte do código que só é executada quando for chamada ***

# ----- VARIÁVEIS -----
nome  = str ( input ('Digite seu nome: '  ) )
idade = int ( input ('Digite sua idade: ' ) )
# ----- VARIÁVEIS -----

# ----- FUNÇÃO -----
def ola_mundo (fnome, fidade):
    print ( 'Olá Mundo' )
    print ( 'Olá ' + nome + '. Você tem: ' + str (idade) + ' anos!' )
# ----- FUNÇÃO -----

ola_mundo(nome, idade)