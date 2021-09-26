# ****** Super() é uma função usada para dar acesso a métodos de uma classe pai.
# retorna um objeto temporareo da ckasse pai quando usada *****

# ===== CLASSES DOS OBJETOS =====
class Retangulo:

    # ===== CONSTRUTOR =====
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura     = largura
    # ===== CONSTRUTOR =====

class Quadrado(Retangulo):
    
    # ===== CONSTRUTOR =====
    def __init__(self, comprimento, largura):
        super().__init__(comprimento, largura)
    # ===== CONSTRUTOR =====

    # ===== MÉTODOS =====
    def area(self):
        return self.comprimento*self.largura
    # ===== MÉTODOS =====

class Cubo(Retangulo):
    # ===== CONSTRUTOR =====
    def __init__(self, comprimento, largura, altura):
        super().__init__(comprimento, largura)
        self.altura = altura
    # ===== CONSTRUTOR =====

    # ===== MÉTODOS =====
    def volume(self):
        return self.comprimento*self.largura*self.altura
    # ===== MÉTODOS =====
# ===== CLASSES DOS OBJETOS =====

# ===== CRIAÇÃO DOS OBJETOS =====
quadrado = Quadrado (5, 5)
cubo     = Cubo     (5, 5, 5)
# ===== CRIAÇÃO DOS OBJETOS =====

print ( quadrado.area() )
print ( cubo.volume() )