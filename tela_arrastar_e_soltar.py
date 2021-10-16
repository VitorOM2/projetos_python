# ==================== Importações ====================
from tkinter import *
# ==================== Importações ====================


# ==================== Funções ====================
def arrastar_inicio(evento):
    rotulo1.inicio_X = evento.x
    rotulo1.inicio_Y = evento.y

def arrastar_movimento(evento): # Pega as novas coordenadas do label
    x = rotulo1.winfo_x() - rotulo1.inicio_X + evento.x
    y = rotulo1.winfo_y() - rotulo1.inicio_Y + evento.y
    rotulo1.place (x = x, y = y) # Atualiza a posição do label

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
rotulo1.bind ( ' <Button-1> ', arrastar_inicio    )
rotulo1.bind ( ' <B1-Motion> ', arrastar_movimento)

# ==================== Configurações ====================


# ==================== Mostrar ====================

# ===== Labels =====
rotulo1.place ( x = 0, y = 0)

# ===== Tela =====
tela.mainloop()
# ==================== Mostrar ====================
