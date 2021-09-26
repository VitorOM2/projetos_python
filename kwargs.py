# *** Kwargs é um parametro que vai agrupar todos os argumentos em um dicionário ***

# ----- FUNÇÕES -----
def ola( **nomes ):
    print ('Olá', end= ' ')

    # ----- For Loop -----
    for key,value in nomes.items():
        print ( value, end= ' ' )
    # ----- For Loop -----
# ----- FUNÇÕES ----- 

ola( nome='Vitor', meio='Oliveira', sobrenome='Marques' )