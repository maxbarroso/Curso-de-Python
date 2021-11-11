# Curso de Python do Curso em Vídeo
# Desafio 04 Aula #06 Tipos primitivos e Saída de dados
# Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo 
# e todas as informações possíveis sobre ele
# Aluno MaxBarroso

a = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(a)}')
print(f'Só tem espaços? {a.isspace()}')
print(f'É um número? {a.isnumeric()}')
print(f'É alfabético? {a.isalpha()}')
print(f'É alfanumérico? {a.isalnum()}')
print(f'Está em maiúsculas? {a.isupper()}')
print(f'Está em minúsculas? {a.islower()}')
print(f'Está capitalizado? {a.istitle()}')