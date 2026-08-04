from filmes import CadastrarFilme, ListarFilme, EditarFilme, FiltrarFilme, ExcluirFilme

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
        CadastrarFilme()

    elif opcao == 2:
        ListarFilme()

    elif opcao == 3:
        EditarFilme()

    elif opcao == 4:
        FiltrarFilme()
              
    elif opcao == 5:
        ExcluirFilme()

    elif opcao == 0:
        print('Finalizando...')
        break

    else:
        print('Opção inválida, tente novamente!') 
print('Até a próxima!')
print('-'* 40)  
