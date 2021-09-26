# *** Cria uma substring extraindo elemento de uma outra string ***
# *** Funciona com index[] ou com slice()                       ***
# *** [inicio:final:pulo]                                       ***

# *** INDEX [] ***
#----- VARIÁVEIS -----
nome = "Vitor Marques"
primeiro_nome = nome [   : 5      ]
sobrenome     = nome [ 6 :        ]
nome_pulando  = nome [   :   :  2 ]
nome_reverso  = nome [   :   : -1 ]
#----- VARIÁVEIS -----

print ( primeiro_nome  )
print ( sobrenome      )
print ( nome_pulando   )
print ( nome_reverso   )
# *** INDEX [] ***

# *** SLICE () ***
#----- VARIÁVEIS -----
site1 = "https//google.com"
site2 = "https//wikipedia.com"
slice = slice(7,-4)
#----- VARIÁVEIS -----

print (site1 [slice] )
print (site2 [slice] )