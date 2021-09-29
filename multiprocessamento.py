# Executa multiplas tarefas em diferente cpu cores.
# Multiprocessing = Melhor para tarefas CPU BOUND (Uso Pesado de CPU)
# Multithreadings = Melhor para tarefas IO BONND  (Esperar)

# ==================== Importações ====================
from multiprocessing import Process, cpu_count
import time
# ==================== Importações ====================

def contador(numero):
    numero_contador = 0

    while numero_contador < numero:
        numero_contador += 1

def main():

    print( cpu_count() ) # Mostra o número de processadores

    a = Process ( target = contador, args = ( 250000000, ) )
    b = Process ( target = contador, args = ( 250000000, ) )
    c = Process ( target = contador, args = ( 250000000, ) )
    d = Process ( target = contador, args = ( 250000000, ) )

    a.start()
    b.start()
    c.start()
    d.start()

    a.join()
    b.join()
    c.join()
    d.join()

    print ('Terminado em: ', time.perf_counter(), " segundos" )

if __name__ == '__main__':
    main()