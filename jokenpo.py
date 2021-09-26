# ===== BIBLIOTECAS =====
import random
# ===== BIBLIOTECAS =====

# ===== LOOP: Jogar =====
while True:
    # ===== VARIÁVEIS =====
    escolhas   = ['pedra', 'papel', 'tesoura']
    computador = random.choice(escolhas)
    jogador    = None
    # ===== VARIÁVEIS =====

    # ===== LOOP: Escolha =====
    while jogador not in escolhas:
        jogador = input ( 'Pedra, Papel ou Tesoura?: '.lower() )
    # ===== LOOP: Escolha =====

    # ===== RESULTADOS =====

    # === Empate ===
    if jogador == computador:
        print ( 'Computador: ' + computador ) 
        print ( 'Você: ' + jogador          )
        print ( '***Empate!***'             )
    # === Empate ===

    # === Pedra ===
    if jogador == 'pedra':
        if computador == 'papel':
            print ( 'Computador: ' + computador ) 
            print ( 'Você: ' + jogador          )
            print ( '***Você perdeu!***'        )
        if computador == 'tesoura':
            print ( 'Computador: ' + computador ) 
            print ( 'Você: ' + jogador          )
            print ( "***Você ganhou!***"        )
    # === Pedra ===

    # === Papel ===
    if jogador == 'papel':
        if computador == 'tesoura':
            print ( 'Computador: ' + computador ) 
            print ( 'Você: ' + jogador          )
            print ( '***Você perdeu!***'        )
        if computador == 'pedra':
            print ( 'Computador: ' + computador ) 
            print ( 'Você: ' + jogador          )
            print ( '***Você ganhou!***'        )    
    # === Papel ===

    # === Tesoura ===
    if jogador == 'tesoura':
        if computador == 'pedra':
            print ( 'Computador: ' + computador ) 
            print ( 'Você: ' + jogador          )
            print ( '***Você perdeu!***'        )
        if computador == 'papel':
            print ( 'Computador: ' + computador ) 
            print ( 'Você: ' + jogador          )
            print ( "***Você ganhou!***"        )
    # === Tesoura ===

    # ===== RESULTADOS =====

    jogar_de_novo = str( input ( 'Jogar de novo? (Sim/Não): ' ).lower() )

    if jogar_de_novo != 'sim':
        break
# ===== LOOP: Jogar =====

print ('Tchau!')