# ==================== Importações ====================
from tkinter import *
from tkinter import ttk
# ==================== Importações ====================


# ==================== Instanciação ====================

# ===== Tela =====
tela = Tk()

# ===== Notebook =====
notebook = ttk.Notebook(tela) # Dispositivo que gerência uma coleção de janelas/displays

tab1 = Frame(notebook) # Novo frame para a tab1
tab2 = Frame(notebook) # Novo frame para a tab2

# ===== Rótulos =====
rotulo_tab1 = Label(tab1,
    text   = 'Tab1',
    width  = 50,
    height = 25)

rotulo_tab2 = Label(tab2,
    text   = 'Tab2',
    width  = 50,
    height = 25)

# ==================== Instanciação ====================


# ==================== Configurações ====================

# ===== Notebook =====
notebook.add(tab1, text = 'Tab 1')
notebook.add(tab2, text = 'Tab 2')

# ==================== Configurações ====================


# ==================== Mostrar ====================

# ===== Notebook =====
notebook.pack(
    expand = TRUE, # Expande para preencher qualquer espaço não utilizad
    fill = 'both') # Preenche espaço nos eixos x e y

# ===== Rótulos =====
rotulo_tab1.pack()
rotulo_tab2.pack()

# ===== Tela =====
tela.mainloop()

# ==================== Mostrar ====================