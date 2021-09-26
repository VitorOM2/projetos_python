# *** Muda a execução dos loops da sequência normal ***

# BREAK    =   Usado para parar um loop completamente.
# CONTINUE =   Pula a proxima interação do loop.
# PASS     =   Funciona como espaço.

# ----- Break -----
#while True:
#    nome = str ( input ( "Digite seu nome: " ) )
#    if nome != "":
#        break

# ----- Continue -----
#num_telefone = "123-456-7890"

#for i in num_telefone:
#    if i == "-":
#        continue
#    print ( i, end = "" )

# ----- Pass -----
for i in range ( 1, 21 ):
    if i == 17:
        pass
    else:
        print ( i )