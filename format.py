# ===== Str Format() serve para dar os usuários mais controle quando for exibir o output =====

# ===== VARIÁVEIS =====

animal = 'aranha'
objeto = 'jarra'
texto  = ' A {} arranhou a {}'
nome   = 'Vitor'
pi     = 3.14159
x      = 1000

# ===== VARIÁVEIS =====

# ===== EXEMPLOS DE FORMAT() EM STRINGS =====

#print ( 'A ' + animal + ' arranhou a ' + objeto          )
#print ( 'A {} arranhou a {}'.format   ( animal, objeto ) )
#print ( 'A {0} arranhou a {1}'.format ( animal, objeto ) )  ** Argumento Posicional **
#print ( 'A {animal} arranhou a {objeto}'.format ( animal='aranha', objeto='jarra' ) )  ** posicionamento das palavras chaves **
print ( texto.format( animal, objeto ) )

# ===== EXEMPLOS DE FORMAT() EM STRINGS =====

# ===== USANDO FORMAT() PARA CRIAR UM ESPAÇO LIMITADO PARA PREENCHIMENTO =====

print ( 'Olá, {:10}. Seja bem vindo'.format  ( nome ) ) # ** {:10} cria um espaço de preenchimento de 10 caracteres.
print ( 'Olá, {:<10}. Seja bem vindo'.format ( nome ) ) # ** {:10} cria um espaço de preenchimento de 10 caracteres com alinhamento a esquerda.
print ( 'Olá, {:>10}. Seja bem vindo'.format ( nome ) ) # ** {:10} cria um espaço de preenchimento de 10 caracteres com alinhamento a direita.
print ( 'Olá, {:^10}. Seja bem vindo'.format ( nome ) ) # ** {:10} cria um espaço de preenchimento de 10 caracteres com alinhamento centralizado.

# ===== USANDO FORMAT() PARA CRIAR UM ESPAÇO LIMITADO PARA PREENCHIMENTO =====

# ===== USANDO FORMAT() PARA FORMATAR NÚMEROS =====

print ( 'O número do pi é: {:.2f}'.format ( pi ) )        # ** {:2f} formata os números reais        **
print ( 'O número é {:,}'.format ( x ) )                  # ** {:,} acrescenta uma virgula no número **
print ( 'O número {0} em binário é: {0:b}'.format ( x ) ) # ** {:b} formata o número em binário      **
print ( 'O número {0} em octais é: {0:o}'.format  ( x ) ) # ** {:o} formata o número em octais       **

# ===== USANDO FORMAT() PARA FORMATAR NÚMEROS =====