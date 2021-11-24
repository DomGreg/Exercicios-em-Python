import random,time
itens = ('Pedra','Papel','Tesoura')
print('-=' * 15)
print("""
CONSEGUE ME VENCER?

[0] Pedra
[1] Papel
[2] Tesoura

""")
print ('-=' * 15)
jogador = int ( input ('Qual a sua jogada:  '))

while jogador <0 or jogador >2:
    jogador = int(input("""
    JOGADA INVALIDA 
    __________________
    ESCOLHA NOVAMENTE: """))

print('JO')
time.sleep (1)
print('KEN')
time.sleep(1)
print("""PO!!!

""")
time.sleep(1)

pc = random.randint(0,2)
print('-_-' * 10)
print('Computador escolheu {}' .format(itens[pc]))
print('O jogador escolheu {}' .format (itens[jogador]))
print('-_-' * 10)

if pc == 0: # computador jogou PEDRA
    if jogador == 0:
        print (' QUEM DIRIA, EMPATAMOS ')

    elif jogador == 1:
        print ('VOCÊ GANHOU')

    elif jogador == 2:
        print ('VOCÊ PERDEU')

    else:
        print ('JOGADA INVÁLIDA')

if pc == 1: # Computador jogou PAPEL
    if jogador == 0:
        print ('VOCÊ PERDEU')

    elif jogador == 1:
        print ('EMPATAMOS')

    elif jogador == 2:
        print ('VOCÊ GANHOU')

    else:
        print('JOGADA INVÁLIDA')

if pc == 2: # Computador jogou TESOURA
    if jogador == 0:
        print('VOCÊ GANHOU')

    elif jogador == 1:
        print('VOCÊ PERDEU')

    elif jogador == 2:
        print ('EMPATAMOS')

    else:
        print('JOGADA INVÁLIDA')