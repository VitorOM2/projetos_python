# *** Região que uma váriavel é reconhecida ***
# ** Uma váriavel é reconhecida apenas dentro da região que ela foi criada **
# * Versões globais e locais de uma váriavel podem ser criadas *

nome = 'Vitor' # ( Váriavel GLOBAL )

def mostrar_nome ():
    nome = 'Marques' # ( Variável LOCAL )
    print (nome)

print ( nome )
mostrar_nome () 