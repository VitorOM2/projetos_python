# Dictionary_comprehensions = cria dicionarios usando uma expressão
#                             pode substituir for loops e certas funções lambda

# ======================================== Exemplo 1 ========================================
temp_cidades_f = {'Nova Iorque': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}

# Dicionário   =  key:        Expressão            for (key,value) in       interable
temp_cidades_c = {key: round( (value-32) * (5/9) ) for (key,value) in temp_cidades_f.items()}

print (temp_cidades_c)
# ======================================== Exemplo 1 ========================================

# ======================================== Exemplo 2 ========================================
clima = {'Nova Iorque': 'Nevando', 'Boston': 'Ensolarado', 'Los Angeles': 'Ensolarado', "Chicago": 'Nublado'}

# Dicionário     =  key: Expressão for (key,value) in interable condicional
clima_ensolarado = {key: value for (key,value) in clima.items() if  value == 'Ensolarado'}

print (clima_ensolarado)
# ======================================== Exemplo 2 ========================================

# ======================================== Exemplo 3 ========================================
cidades = {'Nova Iorque': 0, 'Boston': 24, 'Los Angeles': 38, 'Chicago': 10}

# Dicionário     =  key: (if/else) for (key,value) in interable
desc_cidades = {key: ("Quente" if value >= 20 else "frio")for (key,value) in cidades.items()}

print (desc_cidades)
# ======================================== Exemplo 3 ========================================

# ======================================== Exemplo 4 ========================================
def checar_temperatura(valor):
    if valor >= 30:
        return "Quente"
    elif  29 >= valor >= 20:
        return "Caloroso"
    else:
        return "Frio"

# Dicionário  =  key:       função(value)       for (key,value) in interable
desc_cidades2 = {key: checar_temperatura(value) for (key,value) in cidades.items()}

print (desc_cidades2)
# ======================================== Exemplo 4 ========================================