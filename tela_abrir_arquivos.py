# ==================== Importações ====================
from tkinter import *
from tkinter import filedialog  
# ==================== Importações ====================


# ==================== Funções ====================
# ==================== Funções ====================



# ==================== Instanciação ====================

# ===== Tela =====
tela = Tk()

# ===== Botões =====
btn_abrir_arquivos = Button(
    text    = 'Abrir',
    command = abrir_arquivos)

# ==================== Instanciação ====================


# ==================== Mostrar ====================

# ===== Botões =====
btn_abrir_arquivos.pack

# ===== Tela =====
tela.mainloop()

# ==================== Mostrar ====================