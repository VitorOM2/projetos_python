from os import write


# ===== VARIÁVEIS =====
text = ' ========== Oi ========== \nTenha um bom dia\n'
# ===== VARIÁVEIS =====

with open ('teste2.txt', 'w') as file:
    file.write(text)