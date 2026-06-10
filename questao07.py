jogos = int(input("Quantidade de jogos: "))

vitorias = 0
empates = 0
derrotas = 0
pontos = 0

for i in range(jogos):
    gols_brasil = int(input("Gols do brasil: "))
    gols_argentina = int(input("Gols da argentina: "))

    if gols_brasil > gols_argentina:
        vitorias += 1
        pontos += 3
    elif gols_brasil == gols_argentina:
        empates += 1
        pontos += 1
    else:
        derrotas += 1

print(f"Vitórias: {vitorias}")
print(f"Empates: {empates}")
print(f"Derrotas: {derrotas}")
print(f"Pontuação: {pontos}")
