""" Criar uma classe carro que vai possuir dois tributos composto por outras duas classe:
1) motor
2) direção

Motor terá a responsabilidade de controlar a velocidade
ele oferece os seguintes atributos:
1) atributo de dados velocidade.
2) Método acelerar, que deve´ra incrementar a velocidade de uma unidade
3) Método frear que deverá decrementar a velocidade em duas unidades

A direção terá a responsabilidade a direção. Ela oferece os seguintes atributos:
1) valor de direção com valores possíveis norte, sul, leste, oeste.
2) Método girar à direita
3) Método girar à esqueerda


    exemplos:
    >>> #Testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> #testando direção
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    3
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'

"""

class Carro:
    def __init__(self, direcao, motor):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar

    def frear(self):
        self.motor.frear

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()

NORTE = 'Norte'
SUL ='Sul'
LESTE = 'Leste'
OESTE = 'Oeste'


class Motor:
    def __init__(self):
        self.velocidade = 0
    def acelerar(self):
        self.velocidade += 1
    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)
class Direcao:
    rotacao_a_direita_dct = {NORTE:LESTE, LESTE:SUL, SUL:OESTE, OESTE:NORTE}
    rotacao_a_esquerda_dct = {NORTE:OESTE, OESTE:SUL, SUL:LESTE, LESTE:NORTE}

    def __init__(self):
        self.valor = NORTE
    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dct[self.valor]
    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dct[self.valor]


