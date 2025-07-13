#divisão
print(5 / 4)

#divisão inteira
print(5 // 4)

#resto da divisão
print(6 % 4)

nome_aluno = 'Guilherme'

#tipos da variável
print(type(nome_aluno))
print(type('Gustavo'))

#conversão para maiúscula
print(nome_aluno.upper())

#conversão para minúsculas
print(nome_aluno.lower())

nome_aluno2="     Carlos"
#remover espaços em branco
print(nome_aluno2.split())

ex1="Casa-hotel"
print(ex1.split("-"))

# Exercícios
# Inteiros (int)
# 1-Escreva um programa que soma dois números inteiros inseridos pelo usuário.
number_1=int(input("Digite o primeiro número: "))
number_2=int(input("Digie o segundo núemro inteiro: "))
resultado= number_1 + number_2
print(f'Ex01 - A soma é: {resultado}')

# 2-Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
inf_number= int(input("Informe um número: "))
result_info= (inf_number % 5)
print(f'Ex02 - O resultado do resto da divisão por 5 é: {result_info}')
# 3-Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
inf_mult1 = float(input("Informe o primeiro número da multiplicação: "))
inf_mult2 = float(input("Informe o segundo núemro da multiplicação: "))
result_mult= inf_mult1 * inf_mult2
print(f'Ex03 - O resultado da multificação é: {result_mult}')
# 4-Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
inf_div1 = int(input("Informe o primeiro número da divisão: "))
inf_div2 = int(input("Informe o segundo número da divisão: "))
result_div = inf_div1 // inf_div2
print(f'Ex04 - O resltado entre a divisão dos núemros {inf_div1} por {inf_div2} é: {result_div}')
# 5-Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
inf_quad =  int(input("Informe o número para o calculo do seu quadrado: "))
result_quad = inf_quad ** 2
print(f'Ex05 - O quadrado do número {inf_quad} é: {result_quad}')

# Números de Ponto Flutuante (float)
# 6-Escreva um programa que receba dois números flutuantes e realize sua adição.
inf_float1 = float(input("Informe o primeiro número: "))
inf_float2 = float(input("Informe o segundo número: "))
result_float = inf_float1 + inf_float2
print(f'Ex06 - O resultado é: {result_float}')
# 7-Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# 8-Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# 9-Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# 10-Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
import math
inf_circle = float(input("Informe o raio: "))
result_circle = math.pi * inf_circle ** 2
area_format = "{:.2f}".format(result_circle)
print(f"Ex10 - A área do círculo é: {area_format}")
# forma mais recente de usar
print(f"Ex10 - A área do círculo é: {result_circle:.2f}")

# Strings (str)
# 11-Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# 12-Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# 13-Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# 14-Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

inf_date = input("Informe uma data de acordo com o padrão dd/mm/aaaa: ")
list_date = inf_date.split("/")
print(f'Ex14 - O dia é: {list_date[0]}, o mês: {list_date[1]} e o ano {list_date[2]}')

# 15-Escreva um programa que concatene duas strings fornecidas pelo usuário.

# Booleanos (bool)
# 16-Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17-Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18-Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19-Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20-Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# try-except e if
# 21 - Conversor de Temperatura - Escreva um programa que converta a temperatura de Celsius para Fahrenheit. O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, garantir que a entrada seja numérica, tratando qualquer ValueError. Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.
# 22 - Verificador de Palíndromo - Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). Utilize try-except para garantir que a entrada seja uma string. Dica: Utilize a função isinstance() para verificar o tipo da entrada.
# 23 - Calculadora Simples - Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. Use try-except para lidar com divisões por zero e entradas não numéricas. Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.
# 24 - Classificador de Números - Escreva um programa que solicite ao usuário para digitar um número. Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero". Adicionalmente, identifique se o número é "par" ou "ímpar".
# 25 - Conversão de Tipo com Validação - Crie um script que solicite ao usuário uma lista de números separados por vírgula. O programa deve converter a string de entrada em uma lista de números inteiros. Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.