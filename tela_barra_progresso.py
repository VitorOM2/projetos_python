# ==================== Importações ====================
from tkinter     import *
from tkinter.ttk import *
import time
# ==================== Importações ====================

# ==================== Funções ====================
def baixar():
    pass
# ==================== Funções ====================

# ==================== Instanciação ====================

# ===== Tela =====
tela = Tk()

# ===== Botões =====
btn_download = Button (tela, text = 'Download', command = baixar)

# ==================== Instanciação ====================

# ==================== Mostrar ====================

# ===== Botões =====
btn_download.pack()

# ===== Tela =====
tela.mainloop()

# ==================== Mostrar ====================