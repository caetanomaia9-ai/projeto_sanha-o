# Lista para armazenar o cadastro dos alunos
alunos = []

# Exemplo de cadastro simples de alunos
while True:
    nome = input("Nome do aluno: ")
    idade = int(input("Idade: "))
    cadastro_ativo = input("Possui cadastro ativo? (sim/nao): ").strip().lower() == "sim"

    # Regras de negócio
    if not cadastro_ativo:
        situacao = "Acesso negado"
    elif idade < 14:
        situacao = "Acesso permitido somente com acompanhamento"
    else:
        situacao = "Acesso permitido"

    # Adiciona o aluno cadastrado na lista
    alunos.append({
        "nome": nome,
        "idade": idade,
        "situacao": situacao
    })

    continuar = input("Deseja cadastrar outro aluno? (s/n): ").strip().lower()
    if continuar != "s":
        break

# Exibição do resultado final de todos os alunos cadastrados
print("\n--- SITUAÇÃO DOS ALUNOS ---")
for aluno in alunos:
    print(f"Aluno: {aluno['nome']} \n Situação: {aluno['situacao']}")