from random import randint
from time import sleep

lista = list()
jogos = list()
print('-'*30)
print('    JOGAR NA MEGA     ')
print('-'*30)
quant = int(input('Quantos jogos vc deseja exibir? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-'*3, f'Soteando {quant} Jogos', '-'*10)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}:{l}')
    sleep(1)
print('-'*5, '> Boa Sorte <', '-'*11)
esco = (input('Para encerrar o programa digite 1 '))
while esco != '1':
    esco =(input('Para encerrar o programa digite 1 '))
    if esco == '1':
        break