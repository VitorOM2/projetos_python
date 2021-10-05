# ==================== Importações ====================
from tkinter import *
# ==================== Importações ====================


# ==================== Funções ====================
def enviar():
    print ('Você pediu: ')
    print (listbox.get ( listbox.curselection() ) )
# ==================== Funções ====================


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

# ===== Caixa de entrada =====
caixa_entrada = Entry(tela)

# ===== Botões =====
botao_enviar = Button (tela,
    text    = 'Enviar',
    command = enviar
)

# ==================== Instanciação ====================


# ==================== Mostrar ===================

# ===== List Box =====
listbox.pack()

# ===== Caixa de entrada =====
caixa_entrada.pack()

# ===== Botões =====
botao_enviar.pack()

# ===== tela =====
tela.mainloop()

# ==================== Mostrar ===================
