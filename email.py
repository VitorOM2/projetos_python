# ==================== Importações ====================
import smtplib


# ==================== Variáveis ====================
remetente    = "viktormarque2053@gmail.com"
destinatario = "viktormarque2053@gmail.com"
senha        = ""
assunto      = "Python - teste de E-mail"
corpo        = "Eu escrevi um email"


# ==================== Cabeçario ====================
mensagem = f""" De: {remetente}
Para: {destinatario}
Assunto: {assunto} \n
{corpo}
"""
