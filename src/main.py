from filmes import CadastrarFilmes, Listar, Editar, Filtrar, Excluir

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
        CadastrarFilmes()

    elif opcao == 2:
        Listar()

    elif opcao == 3:
        Editar()

    elif opcao == 4:
        Filtrar()
              
    elif opcao == 5:
        Excluir()

    elif opcao == 0:
        print('Finalizando...')
        break

    else:
        print('Opção inválida, tente novamente!') 
print('Até a próxima!')
print('-'*40)  
