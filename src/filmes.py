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

#inicio do editar! 
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

def ListarFilmes():
    if not filmes:
        print("Nenhum filme encontrado.")
        return

    for filme in filmes:
        print(filme.nome_filme, filme.genero, filme.ano_lancamento, filme.duracao, filme.nota, filme.sinopse)
