num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

menor = num1
maior = num1

if num2 < menor and num2 < num3:
    menor = num2
elif num3 < menor and num3 < num2:
    menor = num3

if num2 > maior and num2 > num3:
    maior = num2
elif num3 > maior and num3 > num2:
    maior = num3

print(f'O menor número entre ({num1},{num2},{num3}) é o {menor:.2f}!')
print(f'O maior número entre ({num1},{num2},{num3}) é o {maior}!')