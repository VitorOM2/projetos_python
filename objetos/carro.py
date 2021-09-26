# ===== OBJETO =====
class Carro:

    rodas = 4

    # ===== CONSTRUTOR =====
    
    def __init__(self, fabricante, modelo, ano, cor):

        # ===== Atributos =====
        self.fabricante = fabricante 
        self.modelo     = modelo
        self.ano        = ano
        self.cor        = cor
        # ===== Atributos =====

    # ===== CONSTRUTOR =====

    # ===== MÉTODOS =====

    def dirigindo(self):
        print ('O {} está sendo dirigido'.format(self.modelo) )

    def parado(self):
        print ('O {} está parado'.format(self.modelo) )

    # ===== MÉTODOS =====    

# ===== OBJETO =====