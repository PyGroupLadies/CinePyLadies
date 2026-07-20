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
    lista_filmes = []

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
        print('ERRO! O ano de lançamento do filme deve ser informado em minutos.')

    duracao = input('Informe o tempo de duração do filme:')

    if duracao.isnumeric():
        lista_filmes.append(duracao) 
    else:
        print('ERRO! Duração deve ser informada em minutos')

    nota = int(input('Informe a nota do filme de 1 a 5: '))
    if nota <1 or nota >5:
        print('Nota inválida! \n Escolha uma nota entre 1 e 5.')

    sinopse = input('Informe a sinopse do filme.\n(Esta opção não é obrigatória!)\n') 
    lista_filmes.append(sinopse)

    '''for id, filme in enumerate(lista_filmes, start=1):
        filme('') == id
        print(f"{id} - {filme}")'''
        # arrumar o id dos filmes

    filme_cadastrado = Filmes(nome_filme, genero, ano_lancamento, duracao, nota, sinopse)
    print(f"Filme '{filme_cadastrado.nome_filme}' cadastrado com sucesso!")

CadastrarFilme()
