class Pessoa:
    olhos = 2

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
    carlos.sobrenome = 'Kadota'
    del carlos.filhos
    carlos.olhos = 1
    del  carlos.olhos
    print(carlos.__dict__)
    print(renzo.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(carlos.olhos)
    print(renzo.olhos)

