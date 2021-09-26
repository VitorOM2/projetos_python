class usuario:
    
    def __init__(self, nome, id):
        self.nome = nome
        self.id   = id

    @classmethod
    def inputs (cls):
        return cls (
        str ( input ("Digite seu nome: ") ),
        int ( input ("Digite o id: ") )
    )

user = usuario.inputs()

print ('Nome: {}'.format(user.nome) )
print ('Id: {}'.format(user.id)     )