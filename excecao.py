# *** Exception é um evento que ocorre durante uma execução que interrompe o progresso do código ***

# ===== TRY_EXCEPTION =====
try:
    numerador   = int ( input ( 'Digite o númerador: '   ) )
    denominador = int ( input ( 'Digite o denominador: ' ) )
    resultado = numerador / denominador
except ZeroDivisionError as e:
    print (e)
    print ('Você não pode dividir por zero!')
except ValueError as e:
    print (e)
    print ('Digite apenas números, por favor!')
except Exception as e:
    print (e)
    print ('Ocorreu um erro!')
else:
    print (resultado)
finally:
    print ('Try_Exception terminado')
# ===== TRY_EXCEPTION =====