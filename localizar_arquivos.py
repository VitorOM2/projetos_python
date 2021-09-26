import os

path = "C:\\Users\\Cliente\\Desktop\\Teste.txt"

if os.path.exists(path):
    print("A localização existe!")
    if os.path.isfile(path):
        print ('é um arquivo')
    elif os.path.isdir(path):
        print ('é um diretório')
else:
    print ("A localização não existe")