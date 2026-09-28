# ============================================================
# ATIVIDADE NÃO PRESENCIAL (ANP) - SISTEMA DE BIBLIOTECA
# Aluno: Ezequiel Pacheco da Silva
# ============================================================

# ALTERAÇÃO 1: Listas declaradas FORA do while principal para não perder os dados salvos
lista_codigos_livros = []
lista_titulos_livros = []
lista_autores_livros = []
lista_anos_livros = []
lista_qtd_livros = []

while True:
    print("\n" + "=" * 30)
    print("      SISTEMA DA BIBLIOTECA")
    print("=" * 30)
    print("1 - Cadastrar Livro")
    print("2 - Listar Livros")
    print("3 - Pesquisar Livro")
    print("4 - Excluir Livro")
    print("5 - Quantidade de Livros")
    print("6 - Sair\n")

    opcao_texto = input("Escolha uma opção: ")

    if opcao_texto.strip() == "":
        print("Erro: O campo não pode ficar vazio!")
        continue
    elif not opcao_texto.isdigit():
        print("Erro: Digite apenas números (1 a 6)!")
        continue

    opcao = int(opcao_texto)
    print()

    # ------------------------------------------------------------
    # OPÇÃO 1: CADASTRAR LIVROS
    # ------------------------------------------------------------
    if opcao == 1:
        print("=" * 30)
        print("      CADASTRO DE LIVROS")
        print("=" * 30)

        while True:
            codigo = input("Digite o código do livro: ").strip()
            if codigo == "":
                print("Erro: O campo código não pode ficar vazio!")
            else:
                break

        while True:
            titulo = input("Digite o título do livro: ").strip()
            if titulo == "":
                print("Erro: O título não deve ser deixado vazio!")
            else:
                break

        while True:
            autor = input("Digite o nome do autor: ").strip()
            if autor == "":
                print("Erro: O autor não deve ser deixado vazio!")
            else:
                break

        while True:
            ano = input("Digite o ano do livro: ").strip()
            if ano == "":
                print("Erro: O ano não deve ser deixado vazio!")
            elif not ano.isdigit():
                print("Erro: O ano deve conter apenas números!")
            else:
                ano = int(ano)
                break

        while True:
            quantidade_texto = input("Quantidade disponível: ").strip()
            if quantidade_texto == "":
                print("Erro: A quantidade não pode ser vazia!")
            elif not quantidade_texto.isdigit():
                print("Erro: A quantidade deve conter apenas números!")
            else:
                quantidade = int(quantidade_texto)
                if quantidade <= 0:
                    print("Erro: A quantidade disponível deve ser maior que 0!")
                else:
                    break

        lista_codigos_livros.append(codigo)
        lista_titulos_livros.append(titulo)
        lista_autores_livros.append(autor)
        lista_anos_livros.append(ano)
        lista_qtd_livros.append(quantidade)

        print(f"\nLivro '{titulo}' cadastrado e salvo com sucesso!")

    # ------------------------------------------------------------
    # OPÇÃO 2: LISTAR LIVROS
    # ------------------------------------------------------------
    elif opcao == 2:
        print("=" * 30)
        print("      LISTA DE LIVROS")
        print("=" * 30)

        if len(lista_titulos_livros) == 0:
            print("Nenhum livro cadastrado até o momento.")
        else:
            # ALTERAÇÃO 2: Exibição estruturada percorrendo as listas pelo índice
            for i in range(len(lista_titulos_livros)):
                print(f"Código: {lista_codigos_livros[i]}")
                print(f"Título: {lista_titulos_livros[i]}")
                print(f"Autor:  {lista_autores_livros[i]}")
                print(f"Ano:    {lista_anos_livros[i]}")
                print(f"Qtd:    {lista_qtd_livros[i]}")
                print("-" * 20)

    # ------------------------------------------------------------
    # OPÇÃO 3: PESQUISAR LIVRO
    # ------------------------------------------------------------
    elif opcao == 3:
        print("=" * 30)
        print("      PESQUISAR LIVRO")
        print("=" * 30)

        termo_pesquisa = input("Digite o título do livro para pesquisar: ").strip()
        encontrado = False  # Flag para controle de busca

        # ALTERAÇÃO 3: Validação clara se o livro foi encontrado ou não
        for i in range(len(lista_titulos_livros)):
            if lista_titulos_livros[i].lower() == termo_pesquisa.lower():
                print("\nLivro encontrado!")
                print(f"Código: {lista_codigos_livros[i]}")
                print(f"Título: {lista_titulos_livros[i]}")
                print(f"Autor:  {lista_autores_livros[i]}")
                print(f"Ano:    {lista_anos_livros[i]}")
                print(f"Qtd:    {lista_qtd_livros[i]}")
                encontrado = True
                break

        if not encontrado:
            print("\nAviso: Nenhum livro correspondente foi encontrado.")

    # ------------------------------------------------------------
    # OPÇÃO 4: EXCLUIR LIVRO
    # ------------------------------------------------------------
    elif opcao == 4:
        print("=" * 30)
        print("      EXCLUIR LIVRO")
        print("=" * 30)

        termo_excluir = input("Digite o título ou código do livro a excluir: ").strip()
        excluido = False

        # ALTERAÇÃO 4: Exclusão sincronizada em todas as listas usando o mesmo índice
        for i in range(len(lista_titulos_livros)):
            if (lista_titulos_livros[i].lower() == termo_excluir.lower() or 
                lista_codigos_livros[i] == termo_excluir):
                
                titulo_removido = lista_titulos_livros[i]
                
                # Remove de todas as listas simultaneamente
                del lista_codigos_livros[i]
                del lista_titulos_livros[i]
                del lista_autores_livros[i]
                del lista_anos_livros[i]
                del lista_qtd_livros[i]
                
                print(f"\nSucesso: O livro '{titulo_removido}' foi excluído!")
                excluido = True
                break

        if not excluido:
            print("\nAviso: Nenhum livro correspondente foi encontrado para exclusão.")

    # ------------------------------------------------------------
    # OPÇÃO 5: QUANTIDADE DE LIVROS (REQUISITO ADICIONADO)
    # ------------------------------------------------------------
    elif opcao == 5:
        print("=" * 30)
        print("    QUANTIDADE DE LIVROS")
        print("=" * 30)
        
        # ALTERAÇÃO 5: Requisito de exibição total de cadastros usando len()
        total_livros = len(lista_titulos_livros)
        print(f"Total de livros cadastrados: {total_livros}")

    # ------------------------------------------------------------
    # OPÇÃO 6: SAIR
    # ------------------------------------------------------------
    elif opcao == 6:
        print("Programa encerrado. Obrigado, até logo!")
        break

    else:
        print("Opção Inválida! Digite um número entre 1 e 6.")