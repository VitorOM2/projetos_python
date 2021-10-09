# ==================== Importações ====================
from tkinter import *
from tkinter import filedialog
# ==================== Importações ====================


# ==================== Funções ====================
def salvar_arquivo():
    pass
# ==================== Funções ====================


# ==================== Instanciação ====================

# ===== Tela =====
tela = Tk()

# ===== Botões =====
btn_salvar = Button(
    text    = 'Salvar',
    command = salvar_arquivo)

# ===== Caixa de texto =====
caixa_texto = Text()

# ==================== Instanciação ====================


# ==================== Mostrar ====================

# ===== Botões =====
btn_salvar.pack()

# ===== Caixa de texto =====
caixa_texto.pack()

# ===== Tela =====
tela.mainloop()

# ==================== Mostrar ====================