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

# ===== Barra de progresso =====
barra = Progressbar (tela, orient = HORIZONTAL, length = 200)

# ==================== Instanciação ====================

# ==================== Mostrar ====================

# ===== Barra de progresso =====
barra.pack( pady = 10 )

# ===== Botões =====
btn_download.pack()

# ===== Tela =====
tela.mainloop()

# ==================== Mostrar ====================