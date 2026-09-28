print("="*30)
print("    SISTEMA DA BIBLIOTECA")
print("="*30)
print()



print("1 - Cadastrar Livros\n2 - Cadastrar Alunos\n3 - Realizar Empréstimo\n4 - Sair\n")

opcao = int(input('Escolha uma opção: '))
print()

if opcao == 1:
    
    
    print("="*30) 
    print("      CADASTRO DE LIVROS")
    print("="*30)
    print()
    1
    
    cadastro_livros = int(input("Quantos livros deseja cadastrar?: "))
    
    for livro in range (1, cadastro_livros +1):
        
        print()
        print(f"=========== Livro {livro} =========== \n")
        print()
        
        codigo = input("Digite o código do livro: ")
        
        if codigo == "":
            print("O campo não pode ficar vazio!")
                    
        else:
            titulo = input("Digite o título do livro: ")
            if titulo == "":
                print("O título não deve ser deixado vazio!")
            
            else:
                autor = input("Digite o nomo do autor: ")
                if autor == "":
                       print("O autor não deve ser deixado vazio!")
        
                else:
                    ano = (input("Digite o ano do livro: "))
                    if ano == "":
                        print("O ano não deve ser deixado vazio!")
                        
                    else:
                        quantidade = int(input("Quantidade disponível: "))
                        if ano == "":
                                    print("O ano não deve ser deixado vazio!")
                        
                        else:
                             if quantidade <= 0:
                                        print("A quantidade disponível deve ser maior que 0!")
                                        
                             else:
                                print()
                                print("Livro Cadastrado com sucesso!")
                                
                                
                                
            

if opcao == 2:
    print("="*30)
    print("      CADASTRO DE ALUNO")
    print("="*30)
    print()
    
    cadastro_aluno = int(input("Quantos Alunos deseja cadastrar: "))
    
    for aluno in range (1, cadastro_aluno +1):
        
        print()
        print(f"=========== ALUNO {aluno} =========== \n")
        print()
        
        matricula = int(input("Matrícula do aluno: "))
        if matricula == "":
            print("Matrícula incorreta!")
            
        else:
            nome = input("Nome do aluno: ")
            if nome == "":
                print("Nome não pode ser vazio!")
                
            else:
                turma = input("Turma: ")
                print("Aluno cadastrado com sucesso!")
                if turma == "":
                    print("O campo turma não pode estar vazio!")
if opcao == 3:
    
    print("="*30)
    print("EMPRÉSTIMO DE LIVRO")
    print("="*30)
    
    codigo_livro = input("Digite o código do livro: ")
    if codigo_livro == "":
        print("O campo código não pode estar vazio: ")
        
    else:
        matricula_livro = input("Digite a matrícula do livro: ")
        if matricula_livro == "": 
            print("O campo Matrícula não pode estar vazio!")
            
        else:
            quantidade_diponivel = int(input("Quantidade disponível: "))
            if quantidade_diponivel == "":
                print("O campo não pode ser vazio!")
                
            elif quantidade_diponivel <= quantidade:
                print("Emprestimo realizado com sucesso!")
                
            else:
                print('Empréstimo não realizado!')
    
if opcao == 4:
    print("Programa encerrado, Obrigado Tchau!! 🖐\n")
    
else:
    print("Opção Inválida, digite uma opção entre 1, 2, 3, e 4\n")
    