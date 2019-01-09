# Variaveis

a = ".........Finalizado com sucesso......"

input_nome = input("Digite seu nome:")

input_idade = int(input("Digite sua idade:"))

input_num1 = float(input("1. Digite um número: "))

input_num2 = float(input("2. Digite um número: "))

input_num3 = float(input("3. Digite um número: "))

input_num4 = float(input("3. Digite um número: "))

input_compra = float(input("3. Digite o valor da compra (R$): "))

input_desconto = float(input("3. Digite o valor do bonus (%): "))

input_desconto = 10


#cauculos
soma = input_num1 + input_num2 + input_num3

soma2 = input_num1 + input_num2

media = (input_num1+input_num2+input_num3+input_num4)/4

medida_cm = input_num1 * 100

quadrado_x = input_num1

cubo_x = input_num1**3

divisao = input_num1/input_num2

metro_quadrado = input_num1 * input_num2

tempo_segundos = (int(input_num1)*86400)+(int(input_num2)*3600)+(int(input_num2)*60)+(int(input_num4))

total_desconto = input_compra*0.9


print(40*"-")
# Exercicio 01

print("Exercicio 1:", a)



# Exercicio 02

print("Exercicio 2: O seu nome é %s" % input_nome)



# Exercicio 03

print("Exercicio 3: O seu nome é %s e sua idade é %s." % (input_nome, input_idade))



# Exercicio 04

print("Exercicio 4: O número %s está armazenado em memória." %input_idade)



# Exercicio 05

print("Exercicio 5: O número %s foi digitado no painel." %input_idade)



# Exercicio 06

print("Exercicio 6: A soma total é ",soma)



# Exercicio 07

print("Exercicio 7: A soma entre %.2f e %.2f é igual %.2f." %(input_num1, input_num2, soma2))



# Exercicio 08

print("Exercicio 8: A média de %2.f,%.2f,%.2f,%.2f é igual a %.2f." %(input_num1,input_num2,input_num3,input_num4,media))



# Exercicio 09

print("Exercicio 9: %.2f metros é igual %.2f centimetros." %(input_num1,medida_cm))



# Exercicio 10

print("Exercicio 10.1: O quadrado de %s é igual a %s." %(input_num1,quadrado_x))

print("Exercicio 10.2: O cubo de %s é igual a %s." %(input_num1,cubo_x))



# Exercicio 11

print("Exercicio 11.1: %.2f dividido por %.2f é igual a %.2f " %(input_num1,input_num2,divisao))

print("Exercicio 11.2: %.2f dividido por %.2f é igual a %i " %(input_num1,input_num2,divisao))



# Exercicio 12

print("Exercicio 12: Para um retangulo de lados %.2f e %.2f a área é igual a %.2f." %(input_num1,input_num2,metro_quadrado))



# Exercicio 13

print("Exercicio 13: %i dias, %i horas, %i minutos e %i segundos equivalem a %i segundos" %(input_num1,input_num2,input_num3,input_num4,tempo_segundos))



# Exercicio 14

print("Exercicio 14: A compra de R$ %.2f com desconto saiu por R$ %.2f." %(input_compra,input_desconto,total_desconto))
print(a)