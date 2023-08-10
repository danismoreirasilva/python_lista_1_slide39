from datetime import date

ano = int(input("Digite o ano: "))

#trecho de código apenas como exemplo
if date.today().year == ano:
    print('Ano atual')
else:
    print('Não é o ano atual')

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} é bissexto!")
else:
    print(f"O ano {ano} não é bissexto!")


