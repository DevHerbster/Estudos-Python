# Contagem de 1 a 10

contador = 1
while contador <= 10:
    print(contador)
    contador += 1



# Somando números até digitar 0

soma = 0
numero = int(input('Digite um número (0 para sair): '))
while numero != 0:
    soma += numero
    numero = int(input('Digite outro número (0 para sair): '))
print('Soma total:', soma)



# Verificador de senha

senha = ''
while senha != '1234':
    senha = input('Digite a senha: ')
print('Acesso permitido.')


# Tabuada de um número

numero = int(input('Digite um número para ver a tabuada: '))
contador = 1
while contador <= 10:
    print(numero, 'x', contador, '=', numero * contador)
    contador += 1

# Média de notas até digitar nota negativa

soma = 0
contador = 0
nota = float(input('Digite uma nota (negativa para encerrar): '))
while nota >= 0:
    soma += nota
    contador += 1
    nota = float(input('Digite outra nota (negativa para encerrar): '))
if contador > 0:
    media = soma / contador
    print('Média das notas:', round(media, 2))
else:
    print('Nenhuma nota válida foi digitada.')