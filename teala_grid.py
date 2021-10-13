# ==================== Importações ====================
from tkinter import *
# ==================== Importações ====================


# ==================== Instanciação ====================

# ===== Tela =====
tela = Tk()

# Grid() = gerenciador geométrico que organiza widgets em uma forma de tabela

# ===== Labels =====
rotulo_nome = Label (tela,
    text = 'Primeiro nome: ',)

# ===== Caixas de entradas =====
caixa_nome = Entry(tela)

# ==================== Instanciação ====================


# ==================== Mostrar ====================

# ===== Labels =====
rotulo_nome.grid(row = 0, column = 0)

# ===== Caixa de entrada =====
caixa_nome.grid(row = 0, column = 1)

# ===== Tela =====
tela.mainloop()

# ==================== Mostrar ====================