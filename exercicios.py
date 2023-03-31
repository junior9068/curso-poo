"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.



numero = input("Digite um número inteiro para saber se é par ou ímpar: ")

if numero.isdigit():
    resto = int(numero) % 2
    if resto == 0:
        print("O número digitado é par")
    else:
        print("O número digitado é impar")
else:
     print("Você não digitou um número inteiro!")

"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.


hora = input("Digite a hora: ")
try:
    hora = int(hora)
    if hora in range(0,12):
        print("Bom dia")
    elif hora in range(12, 17):
        print("Boa tarde")
    elif hora in range(18, 24):
        print("Boa Noite")   
    else:
        print("Hora inválida")
except:
    print("Digite núemros inteiros")
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

nome = input("Digite seu nome: ")

try:
    if len(nome) <= 4:
        print("Seu nome é muito curto")
    elif len(nome) > 4 and len(nome) < 7:
        print("Seu nome é normal")
    else:
        print("Seu nome é muito grande")
except:
    print("Nome inválido")
