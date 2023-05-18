valor = float(input())

if valor <= 2000.00:
    print('Isento')
elif valor >= 2000.01 and valor <=3000.00:
    imposto = (valor-2000)*0.08
    print(f'R$ {imposto:.2f}')
elif valor >= 3000.01 and valor <= 4500.00:
    imposto = (valor - 3000.00)*0.18 + (1000*0.08)
    print(f'R$ {imposto:.2f}')
elif valor > 4500:
    imposto = (valor - 4500)*0.28 + (1500*0.18) + (1000*0.08)
    print(f'R$ {imposto:.2f}')
