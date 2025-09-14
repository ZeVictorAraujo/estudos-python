#1. Considere o seguinte algoritmo, disponível aqui. Acesso em: 30 jul. 2024.
#2. Leia o algoritmo e identifique todas as funções desconhecidas.
#3. Pesquise na documentação do Python para que servem os seguintes comandos: randint, isnumeric e break. Escreva no documento de entrega do desafio o resultado de sua pesquisa.
#4. Entenda para que servem os blocos de comando escritos pelo programador. Explique o que entendeu, indicando o bloco e sua respectiva explicação.
#5. Reescreva o algoritmo utilizando a estrutura for no lugar da estrutura while. 
#6. Reescreva o algoritmo a fim de reduzir o número de linhas de código. Para isso investigue a possibilidade de trocar alguns comandos ou excluir parte do código. 
#7.Proponha uma melhoria ao jogo, dando a ele seu toque pessoal.

from random import randint

print('#### Iníciando Jogo ####')

random = randint(0, 100)
chute = 0;
chances = 10;
while chute != random:
    chute = input('Chute um número entre 0 a 100: ')
    if chute.isnumeric():
        chute = int(chute)
        chances = chances - 1
        if chute == random:
            print('')
            print('Parabéns, você venceu! O número era {} e você ainda tinha {} chances.'.format(random, chances))
            print('')
            break;
        else:
            print('')
            if chute > random:
                print('Você errou!!! Dica: É um número menor.')
            else:
                print('Você errou!!! Dica: É um número maior.')
            print('Você ainda possui {} chances.'.format(chances))
            print('')
        if chances == 0:
            print('')
            print('Suas chances acabaram, você perdeu!')
            print('')
            break;

print('#### Fim do Jogo ####')