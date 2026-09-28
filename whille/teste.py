#contador = 1
#while contador <= 10:
#    print(contador)
#    contador += 1

#contador = 2
#while contador <= 20:
#    print(contador)
#    contador += 2

#total_alunos = int(input("Quantos alunos serão cadastrados? "))
#contador = 1

#while contador <= total_alunos:
#    nome = input(f"Digite o nome do aluno {contador}: ")
#    print(f"Aluno cadastrado: {nome}")
#    contador += 1

opcao = 0
while opcao != 3:
    print("\n--- MENU ---")
    print("1 — Cadastrar livro")
    print("2 — Listar livros")
    print("3 — Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        qtd_livro = int(input("Quantos Livros deseja cadastrar?"))
        
        for livro in range (qtd_livro):
            autor = input("Autor: ")
            if autor == "":
                print("O campo não pode ficar vazio!")
                autor = input("Autor: ")
                
                
            else:
                titulo = input("Titulo:")
                if titulo == "":
                    print("O campo não pode ficar vazio!")
                    titulo = input("Titulo:")
            
        print("Opção 'Cadastrar livro' selecionada.")
    elif opcao == 2:
        print("Opção 'Listar livros' selecionada.")
    elif opcao == 3:
        print("Saindo do programa...")
    else:
        print("Opção inválida! Tente novamente.")