# Curso de Python do Curso em Vídeo
# Desafio 05 Aula #07 Operadores aritiméticos
# Faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada.

# Aluno MaxBarroso
N = int(input('Digite um número para a tabuada: '))
print('Tabuada do: ', N)
cont = 0
while(cont <= 10):
    print(cont, ' x ', N, '= ' ,(cont * N))
    cont = cont + 1
else:
        print('Tabuada de ', N, 'completa.')
        