# Curso de Python do Curso em Vídeo
# Desafio 05 Aula #07 Operadores aritiméticos
# Faça um programa que leia um numero inteiro e mostre na tela seu sucessor e seu antecessor.
# Aluno MaxBarroso

print ('Este programa vai mostrar o sucessor e o antecessor do número que você digitar.')

n1 = int( input('Digite um numero: '))
A = n1 - 1
S = n1 + 1

print('O Antecessor de ', n1, 'é', A, 'e o sucessor é: ', S )

print('Agora mostrando o mesmo resultado usando a função format:')
print('O Antecessor de  {}, é: {}, e o Sucessor é:  {} ' .format(n1, A, S))

