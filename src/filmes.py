lista_filmes = []
filmes = []

class Filmes:
    def __init__(self, nome_filme, genero,ano_lancamento, duracao, nota, sinopse):
        self.nome_filme = nome_filme
        self.genero = genero
        self.ano_lancamento= ano_lancamento
        self.duracao = duracao
        self.nota = nota
        self.sinopse = sinopse

def CadastrarFilme():
    print('Cadastrando filme')
    nota = 0

    nome_filme = input('Digite o nome do filme:')
    lista_filmes.append(nome_filme)

    genero = input('Informe o gênero do filme. \n Ex: Ação|Romance|Drama \n')
    if genero.isalpha() :
        lista_filmes.append(genero) 
    else:
        print('ERRO! Gênero deve ser informado por letras.')

    ano_lancamento = input('Informe o ano de lançamento do filme: ')

    if ano_lancamento.isnumeric() :
        lista_filmes.append(ano_lancamento) 
    else:
        print('ERRO! O ano de lançamento do filme deve ser informado números.')

    duracao = input('Informe o tempo de duração do filme:')

    if duracao.isnumeric():
        lista_filmes.append(duracao) 
    else:
        print('ERRO! A duração deve ser informada em minutos')

    nota = int(input('Informe a nota do filme de 1 a 5: '))
    if nota <1 or nota >5:
        print('Nota inválida! \n Escolha uma nota entre 1 e 5.')

    sinopse = input('Informe a sinopse do filme.\n(Esta opção não é obrigatória!)\n') 
    lista_filmes.append(sinopse)

    filme_cadastrado = Filmes(nome_filme, genero, ano_lancamento, duracao, nota, sinopse)
    lista_filmes.append(filme_cadastrado)

    print(f"Filme '{filme_cadastrado.nome_filme}' cadastrado com sucesso!")
    filmes.append(filme_cadastrado)

    for indice, filme in enumerate(filmes, start=1):
        print(f'{indice} - {filme.nome_filme}')


def ListarFilmes():
    if not filmes:
        print("Nenhum filme encontrado.")
        return

    for filme in filmes:
        print(filme.nome_filme, filme.genero, filme.ano_lancamento, filme.duracao, filme.nota, filme.sinopse)

def FiltrarFilmes():

    if not filmes:
        print("Nenhum filme cadastrado.")
        return

    print("==== Filtrar por ====")
    print("[1] Gênero")
    print("[2] Ano")

    escolha = input("Escolha uma opção: ")    

    if escolha == "1":
        genero_filtro = input("Digite o gênero do filme: ")
        generos_encontrados = list(filter(lambda filme: filme.genero.lower() == genero_filtro.lower() , filmes))
        for filme in generos_encontrados:
            print(filme.nome_filme, filme.genero, filme.ano_lancamento, filme.duracao, filme.nota, filme.sinopse)
    
    elif escolha == "2":
        ano_filtro = input("Digite o ano lançamento do filme: ")
        anos_encontrados = list(filter(lambda filme: filme.ano_lancamento == ano_filtro , filmes))
        for filme in anos_encontrados:
            print(filme.nome_filme, filme.genero, filme.ano_lancamento, filme.duracao, filme.nota, filme.sinopse)
    else:
        print("Opção inválida.")