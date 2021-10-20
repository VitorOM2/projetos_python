class Bola:

    # ==================== Construtor ====================
    def __init__ (self, canvas, x, y, diametro, velocidade_x, velocidade_y, cor):
        self.canvas = canvas
        self.imagem  = canvas.create_oval(x, y, diametro, diametro, fill = cor)  
        # Primeito diametro serve para o diametro
        # O segundo diametro serve para a altura

        self.velocidade_x = velocidade_x
        self.velocidade_y = velocidade_y

    # ==================== Funções ====================
    def mover (self):
        coordenadas = self.canvas.coords ( self.imagem )
        print (coordenadas)

        # Inverte o movimento da imagem se chegar na borda do canvas
        if ( coordenadas[2] >= ( self.canvas.winfo_width() ) or coordenadas[0] < 0 ):
            self.velocidade_x = -self.velocidade_x

        # Inverte o movimento da imagem se chegar na borda do canvas
        if ( coordenadas[3] >= ( self.canvas.winfo_width() ) or coordenadas[1] < 0 ):
            self.velocidade_y = -self.velocidade_y

        self.canvas.move ( self.imagem, self.velocidade_x, self.velocidade_y )  # Movimenta a imagem