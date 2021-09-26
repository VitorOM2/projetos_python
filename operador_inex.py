# *** Dá acesso a uma sequencia de elementos ***

nome = str ( input ("Digite seu nome: ") )

#if ( nome[0].islower() ):
#    nome = nome.capitalize()

primeiro_nome = nome [0:5].capitalize()
sobrenome     = nome [6: ].capitalize()

print ( 'Seu nome é: ' + primeiro_nome )
print ( sobrenome )