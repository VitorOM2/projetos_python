# Reduce() = Aplica uma função a um iterable que reduz para um unico elemento acumulado
# performa uma função nos dois primeiros elementos e repete até ter apenas um valor sobrando.

import functools

# ===== Exemplo 1 =====
letras  = ["O", "L", "A"]
palavra =  functools.reduce ( lambda x,y: x + y, letras ) # O, L, A -> OL, A -> OLA
print (palavra)

# ===== Exemplo 2 =====
fatorial  = [5, 4, 3, 2, 1]
resultado = functools.reduce ( lambda x,y: x * y, fatorial ) # 5, 4, 3, 2, 1 -> 20, 3, 2, 1 -> 60, 2, 1 > 120
print (resultado)     