try:
  with open( 'teste.txt' ) as file:
    print ( file.read() )
except FileNotFoundError as e:
    print (e)
    print ( 'O arquivo não foi encontrado' )