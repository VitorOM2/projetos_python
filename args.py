# *** Args é um parametro que vai agrupar todos os argumentos dentro de um tuple ***

# ----- FUNÇÕES -----
def soma ( *args ):

    adicao = 0

    # ----- For Loop -----
    for i in args:
        adicao += i
    # ----- For Loop -----

    return adicao
# ----- FUNÇÕES -----

print ( soma( 1, 2, 3, 4, 5, 6, 7, 8 ) )