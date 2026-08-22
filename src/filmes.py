filmes = []

class Filmes:
    def __init__(self, id_filme, nome_filme, genero, ano_lancamento, duracao, nota, sinopse):
        self.id = id_filme
        self.nome_filme = nome_filme
        self.genero = genero
        self.ano_lancamento = ano_lancamento
        self.duracao = duracao
        self.nota = nota
        self.sinopse = sinopse

def gerar_novo_id():
    if not filmes:
        return 1
    return max(filme.id for filme in filmes) + 1

def CadastrarFilme():
    print('\n--- Cadastrando filme ---')

    nome_filme = input('Digite o nome do filme: ')

    genero = input('Informe o gênero do filme. \n Ex: Ação|Romance|Drama \n')
    if not genero.isalpha():
         print('ERRO! Gênero deve ser informado por letras.')

    ano_lancamento = input('Informe o ano de lançamento do filme: ')
    if not ano_lancamento.isnumeric():
         print('ERRO! O ano de lançamento do filme deve ser informado em números.')

    while True:
        try:
            duracao = int(input('Informe o tempo de duração do filme em minutos: \n'))
            break
        except ValueError:
            print('ERRO! A duração deve ser informada em números inteiros.')

    while True:
        try:
            nota = int(input('Informe a nota do filme de 1 a 5: '))
            if nota < 1 or nota > 5:
                print('Nota inválida! Escolha uma nota entre 1 e 5.')
            else:
                break
        except ValueError:
            print('ERRO! Digite um número válido.')

    sinopse = input('Informe a sinopse do filme (Opcional): \n')

    id_gerado = gerar_novo_id()

    filme_cadastrado = Filmes(id_gerado, nome_filme, genero, ano_lancamento, duracao, nota, sinopse)

    filmes.append(filme_cadastrado)

    print(f"Filme '{filme_cadastrado.nome_filme}' cadastrado com sucesso com ID {filme_cadastrado.id}!")


def ListarFilmes():
    if not filmes:
        print("Nenhum filme encontrado.")
        return

    for filme in filmes:
        print(f"""
        {{
            "ID":{filme.id},
            "Nome":{filme.nome_filme}, 
            "Genêro":{filme.genero}, 
            "Ano de Lançamento":{filme.ano_lancamento}, 
            "Duração":{filme.duracao}, 
            "Nota":{filme.nota}, 
            "Sinopse":{filme.sinopse}
        }}
            """)

def FiltrarFilmes():

    if not filmes:
        print("Nenhum filme cadastrado.")
        return

    print("==== Filtrar por ====")
    print("[1] Gênero")
    print("[2] Ano")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        filtro = input("Digite o gênero do filme: ").strip().lower()

        resultados = [
            filme for filme in filmes
            if filme.genero.strip().lower() == filtro
        ]

    elif escolha == "2":
        try:
            filtro = int(input("Digite o ano de lançamento do filme: "))
        except ValueError:
            print("Ano inválido.")
            return

        resultados = [
            filme for filme in filmes
            if int(filme.ano_lancamento) == filtro
        ]

    else:
        print("Opção inválida.")
        return

    if not resultados:
        print("Nenhum filme encontrado.")
        return

    for filme in resultados:
        print(f"""
                {{
                    "ID": {filme.id},
                    "Nome": {filme.nome_filme},
                    "Gênero": {filme.genero},
                    "Ano de Lançamento": {filme.ano_lancamento},
                    "Duração": {filme.duracao},
                    "Nota": {filme.nota},
                    "Sinopse": {filme.sinopse}
                }}
              """)

def EditarFilme():
    print('\n--- Editando filme ---')
    
    try:
        id_busca = int(input('Digite o ID do filme que deseja editar: '))
    except ValueError:
        print('ERRO! O ID deve ser um número inteiro.')
        return
      
    filme_encontrado = None
    
    for filme in filmes:
        if filme.id == id_busca:
            filme_encontrado = filme
            break

    if not filme_encontrado:
        print('ID não encontrado!')
        return

    print(f"\nEditando o filme: {filme_encontrado.nome_filme}")
  
    novo_nome = input(f"Nome atual ({filme_encontrado.nome_filme}) -> Novo nome: ")
    if novo_nome != "":
        filme_encontrado.nome_filme = novo_nome

    novo_genero = input(f"Gênero atual ({filme_encontrado.genero}) -> Novo gênero: ")
    if novo_genero != "":
        filme_encontrado.genero = novo_genero

    novo_ano = input(f"Ano atual ({filme_encontrado.ano_lancamento}) -> Novo ano: ")
    if novo_ano != "": 
        if novo_ano.isnumeric():
            filme_encontrado.ano_lancamento = novo_ano
        else:
            print("ERRO! Como o valor não é numérico, o ano antigo será mantido.")

    while True:
        nova_duracao = input(f"Duração atual ({filme_encontrado.duracao} min) -> Nova duração: ")
        if nova_duracao == "":
            break 
        if nova_duracao.isnumeric():
            filme_encontrado.duracao = int(nova_duracao)
            break
        else:
            print("ERRO! A duração deve ser um número inteiro.")

    while True:
        nova_nota = input(f"Nota atual ({filme_encontrado.nota}) -> Nova nota (1 a 5): ")
        if nova_nota:
            break 
        if nova_nota.isnumeric():
            nota_int = int(nova_nota)
            if 1 <= nota_int <= 5:
                filme_encontrado.nota = nota_int
                break
            else:
                print("Nota inválida! Escolha uma nota entre 1 e 5.")
        else:
            print("ERRO! Digite um número inteiro.")

    nova_sinopse = input(f"Sinopse atual ({filme_encontrado.sinopse}) -> Nova sinopse: ")
    if nova_sinopse != "":
        filme_encontrado.sinopse = nova_sinopse

    print("\nFilme atualizado com sucesso!")

def ExcluirFilme():
    print('\n--- Excluindo filme ---')
    
    if not filmes:
        print("Nenhum filme cadastrado para excluir.")
        return

    try:
        id_busca = int(input('Digite o ID do filme que deseja excluir: '))
    except ValueError:
        print('ERRO! O ID deve ser um número inteiro.')
        return

    for filme in filmes:
        if filme.id == id_busca:
            # Confirmação de segurança antes de deletar
            confirmacao = input(f"Tem certeza que deseja excluir '{filme.nome_filme}'? (S/N): ").strip().upper()
            if confirmacao == 'S':
                filmes.remove(filme)
                print(f"Filme '{filme.nome_filme}' excluído com sucesso!")
            else:
                print("Operação cancelada.")
            return

    print('ERRO! Filme com o ID informado não foi encontrado.')