nome = input("Digite o nome do cliente: ")
velocidade = int(input("Velocidade da internet em Mbps: "))
print()

if velocidade <= 50:
    mega = "Plano Básico"
    
elif velocidade <= 199:
    mega = "Plano Intermediário"
    
elif velocidade <= 499:
    mega = "Plano Avançado"

else:
    velocidade >= 500
    mega = "Plano Ultra"
    
print("="*10,"AVALIAÇÃO DE PACOTES", "="*10)
print()
print("Cliente: {}z\nVelocidade: {}\nPlano: {}\n".format(nome, velocidade, mega))