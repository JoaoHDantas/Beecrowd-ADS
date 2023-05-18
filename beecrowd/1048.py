salario = float(input())

if salario >= 0 and salario <= 400.0:
    nvsalario = (salario*0.15)+salario
    reaj = nvsalario - salario
    porc = 15
elif salario > 400.0 and salario <= 800.0:
    nvsalario = (salario)*0.12
    reaj = nvsalario - salario
    porc = 12
elif salario > 800.0 and salario <= 1200.0:
    nvsalario = (salario*0.10)+salario
    reaj = nvsalario - salario
    porc = 10
elif salario > 1200.0 and salario <= 2000.0:
    nvsalario = (salario*0.07)+salario
    reaj = nvsalario - salario
    porc = 7
elif salario > 2000.0:
    nvsalario = (salario*0.04)+salario
    reaj = nvsalario - salario
    porc = 4

print(f'Novo salario: {nvsalario:.2f}')
print(f'Reajuste ganho: {reaj:.2f}')
print(f'Em percentual: {porc} %')
