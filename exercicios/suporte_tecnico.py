nome =  input("Digite o seu nome: ")
print()
print("===== TIPO DO PROBLEMA ======")
print("1-Indisponibilidade total do sitema")
print("2-Sistema funcionando, mas com lentidão ou erros")
print("3-Problema que não impede o trabalho")
print("4-Outros problemas")

tipo = int(input("Qual o tipo do problema: "))
tempo = int(input("Digite o tempo do problema em dias: "))

if tipo == (1):
    prioridade = 'Crítica'
    problema = 'Indisponibilidade total do sitema'

elif tipo == (2):
    prioridade = 'Alta'
    problema = 'Sistema funcionando, mas com lentidão ou erros'
 
elif tipo == (3):
    prioridade = 'Média'
    problema = 'Problema que não impede o trabalho'

else:
    Prioridade = 'Baixa'
    problema = 'Outros problemas'
print()

print("===== RESUMO DO CHAMADO =====")
print()
print("Cliente: {}\nProblema: {}\nTempo do problema: {} Dias\nPrioridade: {}\n".format(nome,problema, tempo, prioridade))