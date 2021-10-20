class Bola:

    # ==================== Construtor ====================
    def __init__ (self, canvas, x, y, diametro, velocidade_x, velocidade_y, cor):
        self.canvas = canvas
        self.imagem  = canvas.create_oval(x, y, diametro, diametro, fill = cor)  # Primeito diametro serve para o diametro
                                                                    # O segundo serve para a altura
        self.velocidade_x = velocidade_x
        self.velocidade_y = velocidade_y

    # ==================== Funções ====================
    def mover (self):
        coordenadas = self.canvas.coords ( self.imagem )
        print (coordenadas)