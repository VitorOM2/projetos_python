# *** Coleção que pode ser alterada, não ordenada e que atribue valores chaves ***

capitais = {
            'Brasil': 'Brasilia',
            'EUA'   : 'Washington DC',
            'India' : 'Nova Delhi',
            'Russia': 'Moscou'
           }

capitais.update ( {'Alemanha': 'Berlim'} )

print (capitais.get    ('Brasil') )
print (capitais.keys   ()         )
print (capitais.values ()         )
print (capitais.items  ()         )

for key,value in capitais.items():
    print (key,value)