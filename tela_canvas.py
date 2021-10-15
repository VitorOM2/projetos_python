# ==================== Importações ====================
from tkinter import *

# ==================== Instanciação da Tela ====================
tela = Tk()

# ==================== Instanciação dos widgets ====================

# ===== Canvas =====
canvas = Canvas ( tela, height = 500, width = 500 )

canvas.create_line ( 0, 0, 500, 500, fill = 'blue', width = 5 ) # Cria um linha (Inicio:x,y, Final:x,y)
canvas.create_line ( 0, 500, 500, 0, fill = 'red' , width = 5 )

# ==================== Mostrar ====================

# ===== Canvas =====
canvas.pack()

# ===== Tela =====
tela.mainloop()