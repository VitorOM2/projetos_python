# *** Operadores Lógicos [and,or,not] são usados para se duas ou mais condições são validas ***

# ----- VARIÁVEIS -----
temperatura = int ( input ( "Qual é a temperatura lá fora?: " ) )
# ----- VARIÁVEIS -----

# ----- IF_STATEMENT -----
if temperatura >= 20 and temperatura <= 30:
    print ( "A temperatura está otima hoje!"   )
elif temperatura < 20 or temperatura > 30:
    print ( "A temperatura não está boa hoje!" )
# ----- IF_STATEMENT -----