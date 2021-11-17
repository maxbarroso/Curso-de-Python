# Curso de Python do Curso em Vídeo
# Desafio 05 Aula #07 Operadores aritiméticos
# Faça um programa que leia a largura de a altura de uma parede e sua área
# e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta 2m²

# Aluno MaxBarroso

print('Vamos te ajudar a calcular a quantidade de tintaque você precisa para pintar uma parede.')
alt = float(input('Digite a altura da parede em metros. (Use . ponto ao invés de vírgula) '))
larg = float(input('Digite a largura da parede da parede em metros. (Use . ponto ao invés de vírgula: '))
area = alt * larg 
tint = area /2
print('A área a ser pintada será: {}' .format(area) )
print('A quantidade de tinta necessária para pintar {} será de {} Litros' .format(area, tint))