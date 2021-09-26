# ***** HIGH ORDER: uma função que permite 
# * 1. Aceitar funções como argurmentos.
# * 2. (return) uma função.

# ===== Exemplo 1 =====
def barulhento(texto):
    return texto.upper()
# -------------------------------
def silencioso(texto):
    return texto.lower()
# -------------------------------
def ola(func):
    texto = func ("Olá")
    print (texto)
# -------------------------------

ola (barulhento)
ola (silencioso)
# ===== Exemplo 1 =====

# ===== Exemplo 2 =====
def divisor(x):
    def dividendo(y):
        return (y / x)
    return dividendo

divir = divisor (2)
print ( divir(10) )
# ===== Exemplo 2 =====