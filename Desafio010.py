km_percorrido = float(input('Digite o kms percorridos do carro alugado: '))
dias_alugado = int(input('Digite os quantos dias o carro ficou alugado: '))
preco_dia = 60* dias_alugado
preco_km = 0.15 * km_percorrido
preco_total = preco_km + preco_dia
print(f'você percorreu: {km_percorrido} KMs ficou {dias_alugado} dias alugados  e o preco total foi {preco_total}')
