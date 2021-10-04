# ==================== Importações ====================
from tkinter import *
# ==================== Importações ====================


# ==================== Funções ====================
def enviar():
    nome_usuario = caixa_entrada.get()
    print ( 'Olá ' + nome_usuario)
    caixa_entrada.config (state = DISABLED)

def deletar():
    caixa_entrada.delete(0, END)

def apagar():
    caixa_entrada.delete ( len( caixa_entrada.get() ) -1, END )
# ==================== Funções ====================



# ==================== Instanciação ====================
tela          = Tk()

# ===== caixas de texto =====
caixa_entrada = Entry(tela,
                    font = ( "arial", 16 ),
                    fg   = "#00ff00",
                    bg   = "black")

# ===== Botões =====
botao_enviar  = Button(tela,
                    text    = "Enviar",
                    command = enviar )

botao_deletar  = Button(tela,
                    text    = "Deletar Tudo",
                    command = deletar )

botao_apagar  = Button(tela,
                    text    = "Apagar",
                    command = apagar )

# ==================== Instanciação ====================


# ==================== Mostrar ====================

# ===== Caixas de texto =====
caixa_entrada.pack (side = LEFT)
# ===== Botões =====
botao_enviar.pack  (side = RIGHT)
botao_deletar.pack (side = RIGHT)
botao_apagar.pack  (side = RIGHT)
# ===== Tela =====
tela.mainloop()

# ==================== Mostrar ====================