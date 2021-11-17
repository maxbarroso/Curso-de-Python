# Curso de Python do Curso em Vídeo
# Desafio 05 Aula #07 Operadores aritiméticos
# Cire um programa que leia quanto uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
# (com a cotação atual: 1 dolar = 5,50)
#
# Aluno MaxBarroso
print('Este programa diz quantos dólares você pode comprar.')
cart = float(input ('Quantos Reais você tem na carteira? ')) #cart seria o valor na carteira
cot = 5.50 #cot seria a cotação
print('A cotação do dólar hoje 16-11-2021 está 5,50')
print('Você consegue comprar {} dólares.' .format(cart / cot) )
