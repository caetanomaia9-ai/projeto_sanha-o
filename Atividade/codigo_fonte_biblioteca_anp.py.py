
livros = []

while True:

    print("\n===== BIBLIOTECA =====")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Pesquisar livro")
    print("4 - Excluir livro")
    print("5 - Sair")
    print("6 - Quantidade de livros")  # ALTERAÇÃO 1: Adicionada a opção 6 conforme a ANP

    opcao = input("Digite uma opção: ")

    if opcao == "1":

        titulo = input("Digite o título: ")
        autor = input("Digite o autor: ")

        livros.append([titulo, autor])

        print("Livro cadastrado!")

    elif opcao == "2":

        print("\n--- LIVROS CADASTRADOS ---")

        if len(livros) == 0:
            print("Nenhum livro cadastrado.")
        else:
            for contador in livros:
                print("Título:", contador[0])
                print("Autor:", contador[1])
                print("-" * 20)

    elif opcao == "3":

        pesquisa = input("Digite o título que deseja pesquisar: ")

        for contador in livros:
            if contador[0].lower() == pesquisa.lower():
                print("Livro encontrado!")
                print("Título:", contador[0])
                print("Autor:", contador[1])
                encontrado = True
                break

        if not encontrado:
            print("Nenhum livro correspondente foi encontrado.")

    elif opcao == "4":

        pesquisa = input("Digite o título que deseja excluir: ")
        
      
        excluido = False

        for contador in livros:
            if contador[0].lower() == pesquisa.lower():
                livros.remove(contador)
                print("Livro excluído!")
                excluido = True
                break

        if not excluido:
            print("Nenhum livro correspondente foi encontrado para exclusão.")

    elif opcao == "5":

        print("Programa encerrado.")
        break


    elif opcao == "6":

        print("Quantidade de livros cadastrados:", len(livros))

    else:

        print("Opção inválida!")