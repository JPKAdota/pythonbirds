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
    >>>  motor = Mortor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade()
    1
    >>> motor.acelerar()
    >>> motor.velocidade()
    2
    >>> motor.acelerar()
    >>> motor.velocidade()
    3
    >>> motor.frear()
    >>> motor.velocidade()
    1
    >>> motor.frear()
    >>> motor.velocidade()
    0
    >>> #testando direção
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'leste'
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
    >>> carro.freiar()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'

"""