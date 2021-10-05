# ==================== Importações ====================
from tkinter import *
# ==================== Importações ====================


# ==================== Funções ====================
def enviar():

    comidas = []

    for i in listbox.curselection():
        comidas.insert( i, listbox.get(i) )

    print ('Você pediu: ')
    for i in comidas:
        print (i)

def adicionar():
    listbox.insert( listbox.size(), caixa_entrada.get() )
    listbox.config( height = listbox.size() )

def deletar():
    listbox.delete ( listbox.curselection() )
    listbox.config( height = listbox.size() )
# ==================== Funções ====================


# ==================== Instanciação ====================
tela = Tk()

# ===== List Box =====
listbox = Listbox(tela,
    bg    = '#f7ffde',
    font  = ('Constantia', 35),
    width = 12,
    selectmode = MULTIPLE
)

listbox.insert(1, 'Pizza')
listbox.insert(2, 'Macarronada')
listbox.insert(3, 'Pão de alho')
listbox.insert(4, 'Sopa')
listbox.insert(5, 'Salada')

listbox.config( height = listbox.size() )

# ===== Caixa de entrada =====
caixa_entrada = Entry(tela)

# ===== Botões =====
botao_enviar = Button (tela,
    text    = 'Enviar',
    command = enviar
)

botao_adicionar = Button (tela,
    text    = 'Adicionar',
    command = adicionar
)

botao_deletar = Button (tela,
    text    = 'Deletar',
    command = deletar
)

# ==================== Instanciação ====================


# ==================== Mostrar ===================

# ===== List Box =====
listbox.pack()

# ===== Caixa de entrada =====
caixa_entrada.pack()

# ===== Botões =====
botao_adicionar.pack()
botao_deletar.pack()
botao_enviar.pack()

# ===== tela =====
tela.mainloop()

# ==================== Mostrar ===================
