#5. Reescreva o algoritmo utilizando a estrutura for no lugar da estrutura while. 
#6. Reescreva o algoritmo a fim de reduzir o número de linhas de código. Para isso investigue a possibilidade de trocar alguns comandos ou excluir parte do código. 
#7.Proponha uma melhoria ao jogo, dando a ele seu toque pessoal.
from random import randint

print('#### Iníciando Jogo ####')
print('##Escolha a dificuldade##')
print('[1] Fácil (50 numeros)')
print('[2] Extremo (100 numeros)')

nivel = input('Escolha a dificuldade: ')
dificuldade = dificuldade = {'1' : 10, '2' : 100}
chances = 10
numero = randint(0, dificuldade.get(nivel, 1))

for tentativa in range(chances):
    if nivel == '1':
        chute = input('Digitum número entre 0 e 50: ')
    if nivel == '2':
        chute = input('Digite um número entre 0 e 100: ')
    else:
        chute = input('Digitum número entre 0 e 50: ')
    

    if not chute.isnumeric():
        print('Entrada inválida. Digite apenas números!')
        continue

    chute = int(chute)

    if chute == numero:
        print(f'\n🎉 Parabéns! Você acertou o número {numero} com {chances - tentativa -1} chances restantes!\n')
        break
    else:
        dica = 'menor' if chute > numero else 'maior'
        print(f'Errou! Dica: o número é {dica} que {chute}.')
        restantes = chances - tentativa - 1
        if restantes:
            print(f'Você ainda tem {restantes} chance(s).\n')
        else:
            print(f'\n💥 Fim de jogo! O número era {numero}.\n')

print('#### Fim do Jogo ####')
    