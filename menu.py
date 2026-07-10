
print('~'* 40)
print(f'{"CINE PY LADIES":^40}')
print('~'*40)

while True:
    print('''Escolha uma das opções abaixo para continuar:
    [1]Cadastrar
    [2]Listar
    [3]Editar
    [4]Filtrar
    [5]Excluir
    [0]Encerrar''')
    opcao = int(input('Escolha sua opção: '))

    if opcao == 1:
        print(f'Cadastrar')

    elif opcao == 2:
        print(f'Listar')

    elif opcao == 3:
        print(f'Editar')

    elif opcao == 4:
        print('''Filtrar por: 
    [1]Ano
    [2]Gênero''')
        escolha = (int(input('Escolha sua opção:')))

    elif opcao == 5:
        print(f'Excluir')

    elif opcao == 0:
        print('Finalizando...')
        break

    else:
        print('Opção inválida, tente novamente!') 
print('Até a próxima!')
print('-'* 40)  

 