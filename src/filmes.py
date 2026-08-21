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

CadastrarFilme()
FiltrarFilmes()