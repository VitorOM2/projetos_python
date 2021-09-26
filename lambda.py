""" * Função Lambda: Função escrita em apenas 1 linha usando lamda com plavra chave
    * aceita qualquer números de argumentos mas apenas uma expressão
    * util se for necessário por cuto periodo de tempo e depois jogada fora (um atalho) """

""" 
Exemplo:
===== Sem lambda =====
def double (x):
    return x * 2 

def multiplicar(x,y):
    return x * y
"""

# ===== Com Lambda =====
#        lambda argumentos : expressão
# 1 Argumento:
dobro = lambda x : x * 2

# 2 Argumentos:
multiplicar = lambda x,y : x * y
     
print ( dobro(5) )
print ( multiplicar(5, 3) )    