# ==================== Importações ====================
from tkinter import *

# ==================== Instanciação da Tela ====================
tela = Tk()

# ==================== Instanciação dos widgets ====================

# ===== Canvas =====
canvas = Canvas ( tela, height = 500, width = 500 )

#canvas.create_line ( 0, 0, 500, 500, fill = 'blue', width = 5 ) # Cria um linha (Inicio:x,y, Final:x,y)
#canvas.create_line ( 0, 500, 500, 0, fill = 'red' , width = 5 )

#canvas.create_rectangle ( 50, 50, 250, 250, fill = 'purple') # Cria um retêngulo/quadrado

#pontos = [250, 0, 500, 500, 0, 500]
#canvas.create_polygon   (pontos, fill = 'orange', outline = 'black', width = 5) # Cria um poligono

canvas.create_arc (0, 0, 500, 500, fill = 'green', start = 360) 
# Cria um arco (as coordenadas define o tamanho)
# Start = é em graus

# ==================== Mostrar ====================

# ===== Canvas =====
canvas.pack()

# ===== Tela =====
tela.mainloop()