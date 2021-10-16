# ==================== Importações ====================
from tkinter import *
# ==================== Importações ====================


# ==================== Funções ====================
def arrastar_inicio(evento):
    rotulo1.inicio_X = evento.x
    rotulo1.inicio_Y = evento.y
# ==================== Funções ====================


# ==================== Instanciação da Tela ====================
tela = Tk()
# ==================== Instanciação da Tela ====================


# ==================== Instanciação dos widgets ====================

# ===== Labels =====
rotulo1 = Label (tela, bg = 'blue', height = 5, width = 10)
# ==================== Instanciação dos widgets ====================


# ==================== Configurações ====================

# ===== Labels =====
rotulo1.bind ( ' <Button-1> ', arrastar_inicio )
# ==================== Configurações ====================


# ==================== Mostrar ====================

# ===== Labels =====
rotulo1.place ( x = 0, y = 0)

# ===== Tela =====
tela.mainloop()
# ==================== Mostrar ====================
