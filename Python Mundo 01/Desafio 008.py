# Curso de Python do Curso em Vídeo
# Desafio 05 Aula #07 Operadores aritiméticos
# Escreva um programa que leia um valor em metros e o exiba ele convertido em centímetros e milimetros
# Aluno MaxBarroso

v = float(input('Digite um valor em metros: '))
cen = v * 100
mil = v * 1000
print('O valor convertido em centímetros é {}cm e o valor convertido em milimetros é {}mil' .format(cen, mil))
