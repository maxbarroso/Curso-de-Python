# Curso de Python do Curso em Vídeo
# Desafio 05 Aula #07 Operadores aritiméticos
# Faça um algorítimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

# Aluno MaxBarroso
print('Black-Py-Day')
print('Este programa te ajuda a saber qual o preço do produto com uma quantidade de desconto em %')
valor = float(input('Digite o valor do produto: '))
desc = float(input('Digite qual o % de desconto: '))

diferenca = desc / 100 * valor
final = valor - diferenca

print('O Valor final do produto é: ', final)



