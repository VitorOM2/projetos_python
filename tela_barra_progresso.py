# ==================== Importações ====================
from tkinter     import *
from tkinter.ttk import *
import time
# ==================== Importações ====================

# ==================== Funções ====================
def baixar():
    task = 10
    x    = 0

    while (x < task ): # Preenche a barra de progresso
        time.sleep(1)
        barra ['value'] += 10
        x += 1
        tela.update_idletasks() # Atualiza a tela a cada alteração

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