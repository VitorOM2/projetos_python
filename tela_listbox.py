# ==================== Importações ====================
from tkinter import *
# ==================== Importações ====================


# ==================== Instanciação ====================
tela = Tk()

# ===== List Box =====
listbox = Listbox(tela,
    bg    = '#f7ffde',
    font  = ('Constantia', 35),
    width = 12,
    
    )

listbox.insert(1, 'Pizza')
listbox.insert(2, 'Macarronada')
listbox.insert(3, 'Pão de alho')
listbox.insert(4, 'sopa')
listbox.insert(5, 'Salada')

listbox.config( height = listbox.size() )

# ==================== Instanciação ====================


# ==================== Mostrar ===================

# ===== List Box =====
listbox.pack()

# ===== tela =====
tela.mainloop()

# ==================== Mostrar ===================
