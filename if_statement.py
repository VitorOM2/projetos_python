# ***É uma parte do código que executara caso uma condição for verdadeira ou falsa***

# ----- VARIÁVEIS -----
idade = int ( input( "Qual é a sua idade?: " ) )
# ----- VARIÁVEIS -----

# ----- IF_STATEMENT -----
if idade == 100:
    print ( "Você é um centenário" )
elif idade >= 18:
    print ( "Você é um adulto!"      )
elif idade < 0:
    print ( "Você não nasceu ainda!" )
else:
    print ( "Você é uma criança!"    )    
# ----- IF_STATEMENT -----