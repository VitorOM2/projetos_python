# Map() = Aplica uma função para cada item de um interable (lista, tuples, etc).

# Map(função, interable)
loja = [("blusa",   20.00),
        ("calças",  25.00),
        ("Jaqueta", 50.00),
        ("Meias",   10.00)] 

converter_dollar = lambda data : (data[0],data[1] / 5.30)

loja_dollar = list( map(converter_dollar, loja) )

for i in loja_dollar:
    print (i)
 