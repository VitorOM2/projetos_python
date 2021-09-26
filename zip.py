# Zip(iterables) = Agrega elementos de dois ou mais iterables (listas, tupple, sets, etc)
#                  cria um objeto zipado com elementos pares guardados em um tuple para cada elemento

nome_usuarios = ['Vitor', 'Fernando', 'Bruna']
senhas        = ("123", '321', 'abc')

usuarios = dict (zip (nome_usuarios, senhas) )

print (type (usuarios) )

for key,value in usuarios.items():
    print (key + ' : ' + value)
 