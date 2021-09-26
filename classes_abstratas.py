# ***** Classes abstratas são classes que contém um ou mais métodos abstratos *****
# * Um método abstrato é um método que tem declaração mas não tem implementação *
# * Previne o usuário de criar um objeto dessa classe *
# * Obriga o usuário a sobrescrever métodos abstratos em uma classe filha *

# ===== BIBLIOTECAS =====
from abc import ABC, abstractmethod
# ===== BIBLIOTECAS =====

# ===== CLASSES =====

# ===== CLASSE ABSTRATA =====
class Veiculo (ABC):
    @abstractmethod
    def vai(self):
        pass
    # ===================
    @abstractmethod
    def parar(args):
        pass
# ===== CLASSE ABSTRATA =====

class Carro (Veiculo):
    def vai(self):
        print ('Você está dirigindo este carro')
    # ===================
    def parar(self):
        print ('Este carro está parado')

class Moto (Veiculo):
    def vai(self):
        print ('Você está pilotando esta moto')
    # ===================
    def parar(self):
        print ('Esta moto esta parada')
# ===== CLASSES =====

carro = Carro()
moto  = Moto()

print ('===================')
carro.vai()
carro.parar()
print ('===================')
moto.vai()
moto.parar()
print ('===================')