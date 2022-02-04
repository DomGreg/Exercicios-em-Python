from random import randint
from time import sleep 

print('-=-'*25)
print ("""
Vamos lá, escolha um número de 1 a 10. 

Se você advinhar no número em que estou pensando,
te revelarei um segredo! 
""")
print('-=-'*25)

#entrada de escolha do jogador
computador = randint(1,10) 
jogador = input ('Essa é sua chance, digite seu número: ')

#sleep para gerar expectativa
sleep(1)
print('aquecendo os motores...')
sleep(1)
print('girando a maçaneta...')
sleep(1)
print('agora vai...\n')
sleep(1)

print ( f'O computador jogou: {computador} e você {jogador}\n' )

if int(jogador) == computador: 
    print('Parece que você é muito bom nesse jogo, você ganhou! \nE como prometido, aqui vai o segredo:\n\nCafé sem açucar é muito bom!')
else:
    print('Não foi dessa vez jogador, você perdeu!\n')

print('Obrigado por Jogar!\n')