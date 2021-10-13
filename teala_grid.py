# ==================== Importações ====================
from tkinter import *
# ==================== Importações ====================


# ==================== Instanciação ====================

# ===== Tela =====
tela = Tk()

# Grid() = gerenciador geométrico que organiza widgets em uma forma de tabela

# ===== Labels =====
rotulo_nome      = Label (tela,
    text = 'Primeiro nome: ')

rotulo_sobrenome = Label (tela,
    text = 'Sobrenome: ')

rotulo_email = Label (tela,
    text = 'Email: ')

# ===== Caixas de entradas =====
caixa_nome      = Entry(tela)
caixa_sobrenome = Entry(tela)
caixa_email     = Entry(tela)

# ==================== Instanciação ====================


# ==================== Mostrar ====================

# ===== Labels =====
rotulo_nome.grid      (row = 0, column = 0)
rotulo_sobrenome.grid (row = 1, column = 0)
rotulo_email.grid     (row = 2, column = 0)

# ===== Caixa de entrada =====
caixa_nome.grid      (row = 0, column = 1)
caixa_sobrenome.grid (row = 1, column = 1)
caixa_email.grid     (row = 2, column = 1)

# ===== Tela =====
tela.mainloop()

# ==================== Mostrar ====================