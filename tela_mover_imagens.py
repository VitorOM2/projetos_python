# ==================== Importações ====================

from tkinter import *
# ==================== Importações ====================


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
# ==================== Configurações ====================


# ==================== Mostrar ====================

# ===== Labels =====
rotulo.place (x = 0, y = 0)

# ===== Tela =====
tela.mainloop()
# ==================== Mostrar ====================