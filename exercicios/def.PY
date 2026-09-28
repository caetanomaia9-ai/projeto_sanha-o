def media_aluno():
    nota01 = float(input("Digite a primeira nota: "))
    nota02 = float(input("Digite a segunda nota: "))
    
    nota_final = (nota01 + nota02) / 2
    
    return nota_final


resultado_final = media_aluno()

print(f"A média final do aluno é: {resultado_final}")