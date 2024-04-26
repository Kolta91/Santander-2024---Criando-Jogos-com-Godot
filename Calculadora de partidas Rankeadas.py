def calc_vitorias(quantidade_vitorias, quantidade_derrotas):
    x = quantidade_vitorias - quantidade_derrotas
    saldo = x
    
    if x == 10:
        return "Ferro"
    elif 11 <= x <= 20:
        return "Bronze"
    elif 21 <= x <= 50:
        return "Prata"
    elif 51 <= x <= 80:
        return "Ouro"
    elif 81 <= x <= 90:
        return "Platina"
    elif 91 <= x <= 100:
        return "Ascendente"
    elif x >= 101:
        return "Imortal"

quantidade_vitorias = int(input('Digite quantas vitorias você possui: '))
quantidade_derrotas = int(input('Digite quantas derrotas você possui: '))

res_vitorias = calc_vitorias(quantidade_vitorias, quantidade_derrotas)

print(f"O Herói tem um saldo de {quantidade_vitorias - quantidade_derrotas} e está no nível de {res_vitorias}")
