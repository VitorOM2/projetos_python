# ==================== Importações ====================
from tkinter import *
from tkinter import messagebox
# ==================== Importações ====================


# ==================== Funções ====================
def clique():
    messagebox.showinfo(title = 'Isto é uma caixa de texto',
        message = 'Olá')
# ==================== Funções ====================


# ==================== Instanciação ====================

# ===== Tela =====
tela = Tk()

# ===== Botões =====
btn_caixa_de_texto = Button(tela,
    command = clique,
    text    = 'Clique aqui')

# ==================== Instanciação ====================


# ==================== Mostrar ===================

# ===== Botões =====
btn_caixa_de_texto.pack()

# ===== Tela =====
tela.mainloop()

# ==================== Mostrar ===================