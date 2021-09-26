# ===== CLASSES =====
class Carro:
    cor = None
# =========================
class Moto:
    cor = None
# ===== CLASSES =====

# ===== FUNÇÕES =====
def mudar_cor (veiculo, cor):
    veiculo.cor = cor
# ===== FUNÇÕES =====

# ===== OBJETOS =====
carro_1 = Carro()
# =========================
carro_2 = Carro()
# =========================
carro_3 = Carro()
# =========================
moto_1  = Moto()
# ===== OBJETOS =====

mudar_cor(carro_1, "vermelho")
mudar_cor(carro_2, "branco"  )
mudar_cor(carro_3, "azul"    )
mudar_cor(moto_1 , "vermelho")

print (carro_1.cor)
print (carro_2.cor)
print (carro_3.cor)
print (moto_1.cor)