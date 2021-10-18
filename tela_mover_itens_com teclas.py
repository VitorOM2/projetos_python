# ==================== Importações ====================

from tkinter import *
# ==================== Importações ====================

# ==================== Funções ====================
def mover_cima (evento):
    rotulo.place ( x = rotulo.winfo_x(), y = rotulo.winfo_y() - 5 ) # Pega as cordenadas e atualiza elas

def mover_baixo (evento):
    rotulo.place ( x = rotulo.winfo_x(), y = rotulo.winfo_y() + 5 )

def mover_tras (evento):
    rotulo.place ( x = rotulo.winfo_x() - 5, y = rotulo.winfo_y() )

def mover_frente (evento):
    rotulo.place ( x = rotulo.winfo_x() + 5, y = rotulo.winfo_y() )
# ==================== Funções ====================



# ==================== Instanciação da Tela ====================

tela = Tk()
# ==================== Instanciação da Tela ====================


# ==================== Instanciação dos widgets ====================


# ===== Labels =====
rotulo= Label (tela, bg = 'blue', width = 2)

# ==================== Instanciação dos widgets ====================


# ==================== Configurações ====================

# ===== Tela =====
tela.geometry ('500x500')
tela.bind ('<w>',     mover_cima   )
tela.bind ('<Up>',    mover_cima   )
tela.bind ('<s>',     mover_baixo  )
tela.bind ('<Down>',  mover_baixo  )
tela.bind ('<a>',     mover_tras   )
tela.bind ('<Left>',  mover_tras   )
tela.bind ('<d>',     mover_frente )
tela.bind ('<Right>', mover_frente )

# ==================== Configurações ====================


# ==================== Mostrar ====================

# ===== Labels =====
rotulo.place (x = 0, y = 0)

# ===== Tela =====
tela.mainloop()
# ==================== Mostrar ====================