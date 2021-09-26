# *** Set é uma coleção onde não é ordenada, não indexada e nem permite valores duplicados ***

talheres    = {"colher", "garfo"}
recipientes = {"prato", "copo"  }

#talheres.remove ("faca")
#recipientes.update      ( talheres    ) # UPDATE = Adiciona itens de uma outra set.
#jantar = talheres.union ( recipientes ) # UNION  = Unifica sets.
#talheres.add            ( "faca"      ) # ADD    = Adiciona itens em uma set.

#print (talheres.difference   ( recipientes ) ) # DIFFERENCE   = Mostra os itens diferentes entre sets.
#print (talheres.intersection ( recipientes)  ) # INTERSECTION = Mostra os itens iguais entre sets.

for x in talheres:
    print (x)