# ==================== Importações ====================
from tkinter import *
from tkinter import colorchooser #Sub módulo
# ==================== Importações ====================


# ==================== Funções ====================
def clicar():
    tela.config (bg = colorchooser.askcolor()[1]) 
# ==================== Funções ====================


# ==================== Instanciação ====================

# ===== Tela =====
tela = Tk()
tela.geometry('420x420')

# ===== Botões =====
btn_mudar_cor = Button(tela,
    text    = 'Mudar de cor',
    command = clicar)

# ==================== Instanciação ====================


# ==================== Mostrar ===================

# ===== Botões =====
btn_mudar_cor.pack()

# ===== Tela =====
tela.mainloop()

# ==================== Mostrar ===================