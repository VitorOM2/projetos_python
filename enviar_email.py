# ==================== Importações ====================
import smtplib


# ==================== Variáveis ====================
remetente    = "email@gmail.com"
destinatario = "email@gmail.com"
senha        = ""
assunto      = "Python - teste de E-mail"
corpo        = "Eu escrevi um email"


# ==================== Cabeçario ====================
mensagem = f""" De: {remetente}
Para: {destinatario}
Assunto: {assunto} \n
{corpo}
"""


# ==================== Conexão ====================
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login ( remetente, senha )
print ( 'Logado' )


# ==================== Enviar email ====================
try:
    server.sendmail (remetente, destinatario, mensagem)
    print ('Email enviado')

except smtplib.SMTPAuthenticationError:
    print('Erro ao se conectar')

