# ==================== Importações ====================
from tkinter     import *
from tkinter.ttk import *
import time
# ==================== Importações ====================


# ==================== Funções ====================
def baixar():
    task = 10
    x    = 0

    while (x < task ): # Preenche a barra de progresso

        time.sleep(1)
        barra ['value'] += 10
        x += 1

        porcentagem.set   ( str (int ( ( x / task ) * 100)  ) + '%' )
        texto_tarefas.set ( str (x) + ' / ' + str (task) + ' tarefas completas' )

        tela.update_idletasks() # Atualiza a tela a cada alteração

# ==================== Funções ====================


# ==================== Instanciação da Tela ====================
tela = Tk()
# ==================== Instanciação da Tela ====================


# ==================== Variáveis Globais ====================
porcentagem   = StringVar()
texto_tarefas = StringVar()
# ==================== Variáveis Globais ====================


# ==================== Instanciação dos widgets ====================
# ===== Botões =====
btn_download = Button (tela, text = 'Download', command = baixar)

# ===== Barra de progresso =====
barra = Progressbar (tela, orient = HORIZONTAL, length = 200)

# ===== Labels =====
rotulo_porcentagem = Label (tela, textvariable = porcentagem)
rotulo_tarefas     = Label (tela, textvariable = texto_tarefas)
# ==================== Instanciação ====================


# ==================== Mostrar ====================
# ===== Barra de progresso =====
barra.pack( pady = 10 )

# ===== Labels =====
rotulo_porcentagem.pack()
rotulo_tarefas.pack()

# ===== Botões =====
btn_download.pack()

# ===== Tela =====
tela.mainloop()
# ==================== Mostrar ====================