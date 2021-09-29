# Daemon threads são threads que rodam de plano de fundo e podem ser paradas antes de terminarem.

# ==================== Importações ====================
import threading
import time
# ==================== Importações ====================

# ==================== Funções ====================
def timer():
    print ()
    contador = 0

    while True:
        time.sleep(1)
        contador += 1
        print ("Logado por: ", contador, " segundos")

# ==================== Funções ====================

x = threading.Thread (target = timer, daemon = True)

print (x.isDaemon)

x.start()
resposta = input ("Deseja sair?" + "\n")
