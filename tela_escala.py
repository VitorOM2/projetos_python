# ==================== Importações ====================
from tkinter import *
# ==================== Importações ====================


# ==================== Funções ====================
def enviar():
    print ('A temperatura está: ' + str( escala.get() ) + ' graus Cº')
# ==================== Funções ====================



# ==================== Instanciação ====================
tela   = Tk()
escala = Scale (tela,
    from_  = 100,
    to     = 0,
    length = 500,
    orient = VERTICAL, # Vertical ou horizontal
    font   = ('arial', 20),
    tickinterval = 10, # Indicadores numéricos
    troughcolor  = '#69EAFF',
    fg           = '#FF1C00',
    bg           = '#111111'
    )

escala.set ( ( ( escala['from'] - escala['to'] ) / 2 ) + escala ['to'] ) # Coloca o valor inicial da escala no meio

botao_enviar = Button(tela,
    text = "Enviar",
    command = enviar)
# ==================== Instanciação ====================


# ==================== Mostrar ===================

# ===== Escalas =====
escala.pack()

# ===== Botões =====
botao_enviar.pack()

# ===== Tela =====
tela.mainloop()
# ==================== Mostrar ====================