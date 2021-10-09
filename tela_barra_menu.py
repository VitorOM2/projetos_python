# ==================== Importações ====================
from tkinter import *
# ==================== Importações ====================


# ==================== Instanciação ====================

# ===== Tela =====
tela = Tk()

# ===== Menu =====
menu_barra   = Menu(tela)
menu_arquivo = Menu(menu_barra,
    tearoff = 0)

# ==================== Instanciação ====================


# ==================== Configurações ====================

# ===== Tela =====
tela.config(menu = menu_barra)

# ===== Menu =====
menu_barra.add_cascade(label = 'Arquivo', menu = menu_arquivo)

menu_arquivo.add_command(label = 'Abrir')
menu_arquivo.add_command(label = 'Salvar')
menu_arquivo.add_separator()
menu_arquivo.add_command(label = 'Sair')

# ==================== Configurações ====================


# ==================== Mostrar ====================

# ===== Tela =====
tela.mainloop()

# ==================== Mostrar ====================