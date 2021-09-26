# ==================== Gerador de Senhas ====================

# ========== Importações ==========
import random 
import string

# ========== Variáveis Globais ==========
# Caracteres que serão usados para formar a senha
alfabeto             = list(string.ascii_letters)
digitos              = list(string.digits)
caracteres_especiais = list("!@#$%^&*()Ç")
caracteres           = list(string.ascii_letters + string.digits + "!@#$%^&*()Ç")

# ========== Funções ==========
def gerar_senha():
    tamanho          = int ( input ("Digite o tamanho da senha: ") )
    quant_alfabeto   = int ( input ("Digite a quantidade de letras da senha: "      ) )
    quant_digitos    = int ( input ("Digite a quantidade de digitos da senha: "     ) )
    quant_especiais  = int ( input ("Digite a quantidade de caracteres especiais: " ) )
    quant_caracteres = quant_alfabeto + quant_digitos + quant_especiais

    if quant_caracteres > tamanho:
        print ("O tamanho de caractreres é maior do que o tamanho  escolhido da senha")
        return

    # Cria uma lista vazia para a senha
    senha = []

    # Escolhe letras aleatórias para senha
    for i in range (quant_alfabeto):
        senha.append(random.choice(alfabeto))

    # Escolhe digitos aleatórios para senha
    for i in range (quant_digitos):
        senha.append(random.choice(digitos))

    # Escolhe caracteres especiais aleatórios para senha
    for i in range (quant_especiais):
        senha.append(random.choice(caracteres_especiais))

    # Se o total de caracteres for menor do que tamanho da senha  vai adicionar caracteres aleatórios 
    if quant_caracteres < tamanho:
        random.shuffle(caracteres)  

        for i in range (tamanho - quant_caracteres):    
            senha.append( random.choice (caracteres) )

    # Mistura os caracteres da senha
    random.shuffle(senha)

    # Converte lista para String e imprime na tela
    print ('Senha gerada: ' + "".join( senha ) )

# ========== Chama as Funções ==========
gerar_senha()