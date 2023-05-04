def calcular_distribuicao_otima(valor):
    notas_disponiveis = [100, 50, 20, 10, 5, 2, 1]
    distribuicao_notas = {}
    for nota in notas_disponiveis:
        if valor >= nota:
            distribuicao_notas[nota] = valor // nota
            print(distribuicao_notas[nota])
            valor -= distribuicao_notas[nota] * nota
            print(nota)
    return distribuicao_notas

valor_solicitado = int(input("Digite o valor da quantia solicitada: "))
distribuicao_notas = calcular_distribuicao_otima(valor_solicitado)

print("Distribuição das notas:")
for nota, quantidade in distribuicao_notas.items():
    print(f"{quantidade} notas de R$ {nota:.2f}")