amigos = [("Jose",  17 ),
          ("Maria", 19 ),
          ("Pedro", 18 ),
          ("Marcos", 21)]

idade = lambda data : data[1] >= 18

maiores_idade = list( filter (idade, amigos) )

for i in maiores_idade:
    print (i)