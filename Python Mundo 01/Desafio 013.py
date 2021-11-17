# Curso de Python do Curso em Vídeo
# Desafio 05 Aula #07 Operadores aritiméticos
# Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento# preço com 5% de desconto.

# Aluno MaxBarroso
print('Black-Py-Day')
print('Este programa te ajuda a saber qual o novo salário de um funcionário acrescentando uma porcentagem')
salario = float(input('Digite o Salário do funcionário: '))
desc = float(input('Digite qual a % de acréscimo: '))

diferenca = desc / 100 * salario
final = salario + diferenca

print('O novo salário do funcionario é: ', final)
