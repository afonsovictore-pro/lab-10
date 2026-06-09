jogos = int(input("Quantidade de jogos: "))

vitorias = 0
empates = 0
derrotas = 0
pontos = 0

for i in range(jogos):
    gols_galo = int(input("Gols do Galo: "))
    gols_oponente = int(input("Gols do adversário: "))

    if gols_galo > gols_oponente:
        vitorias += 1
        pontos += 3
    elif gols_galo == gols_oponente:
        empates += 1
        pontos += 1
    else:
        derrotas += 1

print(f"Vitórias: {vitorias}")
print(f"Empates: {empates}")
print(f"Derrotas: {derrotas}")
print(f"Pontuação: {pontos}")
