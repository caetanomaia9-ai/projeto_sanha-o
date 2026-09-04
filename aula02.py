nome = input("Informe seu nome: ")
idade = int(input("Informwe sua idade: "))
altura = float(input("Informe sua altura: "))

print("O nome informado foi: {0} \n A idade informada foi: {1} \n A altura Informada foi: {2}".format(nome,idade,altura))

if idade >= 18:
    print("Voto Obrigatório!!")
elif idade >= 16:
    print("Voto não obrigatório!")
else:
    print("Ainda não pode votar!")
