# ==================== Importações ====================
from tkinter import *
# ==================== Importações ====================

# ==================== Funções ====================
def enviar_texto():
    texto = caixa_texto.get ( '1.0', END)
    print (texto)
# ==================== Funções ====================


# ==================== Instanciação ====================

# ===== tela =====
tela = Tk()

# ===== Caixa de texto =====
caixa_texto = Text(tela)

# ===== Botão =====
btn_enviar = Button(tela,
    text    = 'Enviar',
    command = enviar_texto)

# ==================== Instanciação ====================


# ==================== Mostrar ===================

# ===== Caixa de texto =====
caixa_texto.pack()

# ===== Botão =====
btn_enviar.pack()

# ===== Tela =====
tela.mainloop()

# ==================== Mostrar ===================