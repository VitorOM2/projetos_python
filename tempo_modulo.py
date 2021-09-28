# =============== Importações ===============
import time
# =============== Importações ===============

print ( time.ctime(0) ) # Converte uma expressão de tempo em segundos desde epoch para uma string
                        # Epoch: Quando o computador acha que o tempo começou (ponto de referência)

print ( time.time() )   # Retorna a quantidade atual de segundos desde o epoch

# =============== Data Atual ===============
# Exemplo 1:
# print ( time.ctime( time.time() ) )

# Exemplo 2:
objeto_tempo = time.localtime()
print (objeto_tempo)
tempo_local = time.strftime (" %d %B %Y %H:%M:%S", objeto_tempo)
print (tempo_local)
