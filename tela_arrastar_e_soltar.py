# ==================== Importações ====================
from tkinter import *
# ==================== Importações ====================


# ==================== Funções ====================
def arrastar_inicio(evento):
    widget = evento.widget
    widget.inicio_X = evento.x
    widget.inicio_Y = evento.y

def arrastar_movimento(evento): # Pega as novas coordenadas do label
    widget = evento.widget
    x = widget.winfo_x() - widget.inicio_X + evento.x
    y = widget.winfo_y() - widget.inicio_Y + evento.y
    widget.place (x = x, y = y) # Atualiza a posição do label

# ==================== Funções ====================


# ==================== Instanciação da Tela ====================
tela = Tk()
# ==================== Instanciação da Tela ====================


# ==================== Instanciação dos widgets ====================

# ===== Labels =====
rotulo1 = Label (tela, bg = 'blue', height = 5, width = 10)
rotulo2 = Label (tela, bg = 'red',  height = 5, width = 10)
# ==================== Instanciação dos widgets ====================


# ==================== Configurações ====================

# ===== Labels =====
rotulo1.bind ( ' <Button-1> ', arrastar_inicio    )
rotulo1.bind ( ' <B1-Motion> ', arrastar_movimento)

rotulo2.bind ( ' <Button-1> ', arrastar_inicio    )
rotulo2.bind ( ' <B1-Motion> ', arrastar_movimento)

# ==================== Configurações ====================


# ==================== Mostrar ====================

# ===== Labels =====
rotulo1.place ( x = 0,   y = 0)
rotulo2.place ( x = 100, y = 100)


# ===== Tela =====
tela.mainloop()
# ==================== Mostrar ====================
