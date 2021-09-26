# ===== FUNÇÕES =====

# ===============
def novo_jogo():
    
    respostas_jogador  = []
    respostas_corretas = 0
    num_perguntas      = 1

    # ===== Imprime as perguntas =====
    for key in perguntas:
        print ('==========')
        print (key)
        # ===== Imprime as opções =====
        for i in opcoes[num_perguntas-1]:
            print(i)
        # ===== Imprime as opções =====

        # ===== Recebe as respostas do jogador =====
        resp = input ("Digite (A,B,C ou D): ")
        resp = resp.upper()
        respostas_jogador.append(resp)
        # ===== Recebe as respostas do jogador =====

        # ===== Chama a função de verificar as respostas =====
        respostas_corretas += verificar_respostas(perguntas.get(key), resp)
        # ===== Chama a função de verificar as respostas =====

        num_perguntas += 1
    # ===== Imprime as perguntas =====

    apresentar_pontuacao(respostas_corretas,resp)

# ===============
def verificar_respostas(resp_correta, resp):
    if resp == resp_correta:
        print ('Certa resposta!')
        return 1
    else:
        print ('Resposta Errada"')
        return 0

# ===============
def apresentar_pontuacao(resp_cor, resp_pon):
    print("=========================")
    print("RESULTADOS")
    print("=========================")

    # ===== Imprime as respostas corretas =====
    print("Respostas corretas: ", end="")
    for i in perguntas:
        print(perguntas.get(i), end=" ")
    print()
    # ===== Imprime as respostas corretas =====

    # ===== Imprime as respostas do jogador =====
    print("Suas respostas: ", end="")
    for i in resp_pon:
        print(i, end=" ")
    print()
    # ===== Imprime as respostas do jogador =====

    # ===== Imprime a pontuação =====
    pontuacao = int ( ( resp_cor / len(perguntas) ) * 100 )
    print ('sua pontuação foi: {}% '.format(pontuacao))
    # ===== Imprime a pontuação =====

# ===============
def jogar_novamente():
    resposta = input ('Você quer jogar de novo? (S/N): ')
    resposta = resposta.upper()
    
    if resposta == 'S':
        return True
    else:
        return False
# ===============

# ===== FUNÇÕES =====

# ===== PERGUNTAS =====
perguntas = { # Dicionário para apresentar a pergunta e a resposta correta (KEY)
    'Quem criou o python?'                             : 'A',
    'Que ano a linguagem python foi criada?'           : 'B',
    'Python está associada com qual grupo de comédia?' : 'C',
    'A terra é redonda?'                               : 'A'
    }
# ===== PERGUNTAS =====

# ===== OPÇÕES =====
opcoes = [  
            ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
            ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
            ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
            ["A. Verdadeiro","B. Falso", "C. As Vezes", "D. Não. É em formato de dinossauro"]
        ]
# ===== OPÇÕES =====

# ===== Inicia o jogo =====
novo_jogo()
# ===== Inicia o jogo =====

# ===== Reincia o jogo =====
while jogar_novamente():
    novo_jogo()
# ===== Reincia o jogo =====