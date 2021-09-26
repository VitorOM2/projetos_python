# *** É um container de um dado atribuido na memória do computador ***

#----- VARIÁVEIS -----
primeiro_nome = 'Vitor' #*String: Precisa de aspas "" ou aspas simples '
sobrenome     = 'Marques'
nome_completo = primeiro_nome + " " + sobrenome
idade         = 20
altura        = 1.65
humano        = False 
#----- VARIÁVEIS -----

print ("Olá " +   nome_completo            )
print (type (primeiro_nome)                ) # Type serve para mostrar o tipo da variável
print ("Idade: "  + str(idade)             )
print (type (idade)                        ) 
print ("Altura: " + str(altura) + " metros")
print (type (altura)                       )
print ("Humano:" +  str(humano)            )
print (type (humano)                       )