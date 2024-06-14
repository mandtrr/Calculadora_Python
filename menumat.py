n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
opcao = 0
while opcao !=5:
    print('Qual é a sua opção? \
    [ 1 ] SOMAR \
    [ 2 ] MULTIPLICAR \
    [ 3 ] MAIOR \
    [ 4 ] NOVOS NÚMEROS \
    [ 5 ] SAIR DO PROGRAMA')
    opcao = int(input('Qual é a sua opçao?'))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre os números é de {soma}')
    elif opcao == 2:
        multi = n1 * n2
        print(f'O resultado de {n1} x {n2} = {multi}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print(f'Entre {n1} e {n2}, o maior valor é {maior}')
        else:
            maior2 = n2
            print(f'Entre {n1} e {n2}, o maior valor é {maior2}')
    elif opcao == 4:
        print('Digite os números novamente.')
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    elif opcao == 5: 
        print('Fim do programa.')
    else:
        print('Opção incorreta. Tente novamente.')
