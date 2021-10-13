# ==================== Importações ====================
from tkinter import *
# ==================== Importações ====================


# ==================== Instanciação ====================

# ===== Tela =====
tela = Tk()

# ===== Grid ===== Grid() = gerenciador geométrico que organiza widgets em uma forma de tabela

# ===== Labels =====
rotulo_nome = Label (tela,
    text = 'Primeiro nome: ',)

# ==================== Instanciação ====================


# ==================== Mostrar ====================

# ===== Labels =====
rotulo_nome.pack()

# ===== Tela =====
tela.mainloop()

# ==================== Mostrar ====================