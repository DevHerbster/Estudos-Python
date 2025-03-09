# Verificador de Maioridade

idade = int(input('Digite a sua idade: '))

if idade >= 18:
    print('Você é maior de idade.')
else:
    print('Você é menor de idade.')


# Número Positivo ou Negativo

numero = float(input('Digite um número: '))

if numero > 0:
    print('O número é positivo.')
elif numero < 0:
    print('O número é negativo.')
else:
    print('O número é zero.')



# Aluno Aprovado ou Reprovado

nota = float(input('Digite a nota do aluno: '))

if nota >= 6:
    print('Aluno aprovado.')
else:
    print('Aluno reprovado.')


# Par ou Ímpar

numero = int(input('Digite um número inteiro: '))

if numero % 2 == 0:
    print('O número é par.')
else:
    print('O número é ímpar.')



# Maior Número

numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))

if numero1 > numero2:
    print(f'O maior número é {numero1}.')
elif numero2 > numero1:
    print(f'O maior número é {numero2}.')
else:
    print('Os dois números são iguais.')