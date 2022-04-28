class Pessoa:
    def __init__(self, *filhos,  nome=None, idade=35 ):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    renzo = Pessoa(nome = 'Renzo')
    carlos = Pessoa(renzo, nome = 'Carlos')
    print (Pessoa.cumprimentar(carlos))
    print (id(carlos))
    print (carlos.cumprimentar())
    print (carlos.nome)
    print (carlos.idade)
    for filhos in carlos.filhos:
        print(filhos.nome)
