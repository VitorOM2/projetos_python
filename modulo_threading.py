# thread =  Uma sequência de execuções. Igual uma ordem separada de execuções.
#                  No entanto, cada thread executa um turno para atingir a simultaneidade
#                  GIL = (global interpreter lock),
#                  Permite apenas uma thread de segurar o controle do interpretador do Python por vez

# cpu bound = programa / tarefa que passa a maior parte do tempo esperando por eventos internos (CPU intensive)
#                   usa multiprocessing

# io bound = programa / tarefa que passa a maior parte do tempo esperando por eventos externos (user input, web scraping)
#                   usa multithreading

# ==================== Importações ====================
import threading
import time
# ==================== Importações ====================

# ==================== Funções ====================
def comer_cafe_da_manha():
    time.sleep(3)
    print ("Você comeu o café da manha")
    
def beber_cafe():
    time.sleep(4)
    print ("Você bebeu o seu café")

def estudar():
    time.sleep(5)
    print ("Você terminou de estudar")
# ==================== Funções ====================

# ==================== Threadings ====================
x = threading.Thread (target = comer_cafe_da_manha, args= () )
x.start()

y = threading.Thread (target = beber_cafe, args= () )
y.start()

z = threading.Thread (target = estudar, args= () )
z.start()
# ==================== Threadings ====================

# ==================== Imprimir na tela ====================
# Sincroniza as threadings.
x.join() 
y.join()
z.join()

print ( threading.active_count() ) # Mostra na tela o número de treading sendo executadas.
                                   # Por a threads ja terem sido executadas só vai mostrar um thread.
print ( threading.enumerate()    ) # Lista as threadings sendo executadas.
print ( time.perf_counter()      )
# ==================== Imprimir na tela ====================