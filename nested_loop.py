# *** Um loop dentro de outro loop ***

linhas  = int ( input ( "Quantas linhas?: "  ) )
colunas = int ( input ( "Quantas colunas?: " ) )
simbolo = ( input ( "Entre com o simbolo que quer usar: " ) )

for i in range ( linhas ):
    for j in range ( colunas ):
        print ( simbolo, end = "" )
    print ()