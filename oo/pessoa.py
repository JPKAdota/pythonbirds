class Pessoa:
    olhos = 2

    def __init__(self, *filhos,  nome=None, idade=35 ):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é:  {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe} Aperto de mão'

class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    renzo = Mutante(nome = 'Renzo')
    carlos = Homem(renzo, nome = 'Carlos')
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
    print(Pessoa.olhos)
    print(carlos.olhos)
    print(renzo.olhos)
    print(Pessoa.metodo_estatico(), carlos.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), carlos.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(renzo, Pessoa))
    print(isinstance(renzo, Homem))
    print(renzo.olhos)
    print(carlos.cumprimentar())
    print(renzo.cumprimentar())


