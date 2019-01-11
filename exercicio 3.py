# -*- coding: utf-8 -*-

         #==============python aulas================
         #==============evolutionwebdon=============
         #==========================================
num = int(input("Check se o numero e positivo negativo ou 0 e se e par ou impar \ndigite um numero :"))




if (num == 0):
    print("O número é igual a 0")
if (num < 0):
    print("O número %i é negativo!" %(num))
else:
    print("O número %i é positivo!"%(num))
print(30*"-")
#check par ou impar


if (num%2 ==0):
    print("O número %i é par" %(num))
else:
    print("O número %i é impar!" %(num))
#=====================================
print(30*"-")
print()

#check maior
print(30*"-")
print()

num1 = int(input("Check qual dos dois numeros e maior  \ndigite um numero :"))
num2 = int(input("digite outro numero :"))
print()
#check maior ou menor numero
print(30*"-")
print()



if(num1 > num2):
    print(" primeiro numero que vc digitou foi %i que e maior que %i" %(num1, num2))
else:
    print("segundo numero que vc digitou foi %i que e maior que %i" %(num2, num1))
#=====================================
print(30*"-")
print()
#check maior de idade ou menorprint(30*"-")
print()
#check maior de idade ou menor

print(30*"-")
print()
print()

print(30*"-")
print()
print()
idade = int(input("check se pode transar  \nDigite sua idade :"))
idade_permitida = 18
if(idade<18):
    print("vc nao  pode transar vc precisa ser maior que %i" %(idade_permitida))
else:
    print("parabens vc ja pode transar a idade minima permitida para transar e %i se divirta kkkk" %(idade_permitida))
print(30*"-")
print()

#check midade da mae e filho caucule
print("check idade da mae e do filho calcule quantos anos a mae tinha quando teve o filho")
print(30*"-")
print()

sua_idade = int(input("digite sua idade : "))
idade_mae = int(input("digite a idade da sua mae :"))
soma = idade_mae - sua_idade

print("sua mae tinha %i anos quando teve vc" %(soma))
print(50*"-")

digite1 = int(input("peça dois números, imprima o maior e, em seguida, o menor.\ndigite um numero"))
digite2 = int(input("digite outro  numero"))

if(digite1>digite2):
    print("%i é o número maior" %(digite1))
    print("%i é o número menor" %(digite2))
elif(digite1<digite2):
    print("%i é o número maior" %(digite2))
    print("%i é o número menor" %(digite1))
else:
    if(digite1==digite2):
        print("O número %i é igual ao número %i" %(digite1, digite2))


inteiro_num = input("check se o numero digitado e um numero inteiro\ndigite um numero :")


# A variavel y serve de auxilio para realizar o calculo e a logica para validar se é inteiro ou não
inteiro_num = float(inteiro_num)
y = int(inteiro_num)

print('O valor inserido é um número inteiro {}'.format(
    y) if inteiro_num - y == 0
      else 'O valor inserido não é um número inteiro: {}'.format(inteiro_num))


num_str = input("Check se o valor digitado e string \nDigite oque quiser: ")
if type(num_str)==str:
  print("O valor digitado e uma string!")
else:
  print("O valor nao e uma string")

retry = True
while (retry):
    retry = False
    try:
        tmp = input("Entre um número inteiro:")
        a = int(tmp)
    except ValueError:
        try:
            a = float(tmp)
        except ValueError:
            print("Não é um número")
            retry = True

if (type(a) == float):
    print("É decimal")
elif (type(a) == int):
    print("É inteiro")

numero_um = int(input("Check qual e o maior de 3 numeros digitados\ndigite o primeiro numero :"))
numero_dois = int(input("digite o segundo numero :"))
numero_tres = int(input("digite o terceiro numero :"))

if(numero_um>=numero_dois and numero_tres<=numero_um):
    print("dos 3 numeros digitado o maior foi %i" %(numero_um))
elif(numero_dois>=numero_um and numero_tres<=numero_dois):
    print("dos 3 numeros digitado o maior foi %i" %(numero_dois))
elif(numero_tres>numero_um and numero_dois<=numero_tres):
    print("dos 3 numeros digitado o maior foi %i" %(numero_tres))

num1 = int(input('Check o valor dos 3 numeros e imprimir em modo crescente\nDigite o primeiro numero: '))
num2 = int(input('Didite o segundo numero: '))
num3 = int(input('Digite o terceiro numero: '))

numeros = [num1, num2, num3]
numeros.sort(key=int)

print(numeros)

vogal = list("aeiou")
letras = input("Check se a letra digitada e uma vogal \nDigite uma letra: ")
if letras in list (vogal):
    print("Você digitou uma vogal!!! ")
else:
    print("Não é uma vogal!!")

cilabas = list("bcdfghjlmnpqrstvxz")
letras = input("Check se a letra digitada e uma cilaba \nDigite uma letra: ")
if letras in list (cilabas):
    print("Você digitou uma cilaba!!! ")
else:
    print("Não é uma cilaba!!")

#================================================
#de 0 à 127 são classe A, de 128 a 191 são classe B, de
# 192 a 223 são classe C, de 224 à 239 são classe D
# e a partir de 240 são classe E. Faça um algoritmo que
# leia o primeiro octeto, no formato decimal de um endereço IP, e informe a sua classe.
#====================================================================================
ip = str(input("Digite um endereço IP: "))

posicao = int((ip[:3]))

if (posicao <= 127):
    print("O IP digitado é de classe A")
elif (posicao > 127 and posicao <= 191):
    print("O IP digitado é de classe B")
elif (posicao > 191 and posicao <= 223):
    print("O IP digitado é de classe C")
elif (posicao > 223 and posicao <= 239):
    print("O IP digitado é de classe D")
elif (posicao > 240):
    print("O IP digitado é de classe E")
#===============================data aqui===============================
# 17_Faça um algoritmo que receba um número inteiro, que represente um determinado mês do ano, e mostre o nome do mes deverá exibir:
# fevereiro. O algoritmo também deve validar se a entrada está correta.
mes = input('Check nome do mes correspondente ao numero de data\nDigite o número do mês: ')
if (mes.isnumeric()) == True:
    if mes == '1':
        print ('Janeiro')
    elif mes == '2':
        print ('Fevereiro')
    elif mes == '3':
        print ('Março')
    elif mes == '4':
        print ('Abril')
    elif mes == '5':
        print ('Maio')
    elif mes == '6':
        print ('Julho')
    elif mes == '7':
        print ('Julho')
    elif mes == '8':
        print ('Agosto')
    elif mes == '9':
        print ('Setembro')
    elif mes == '10':
        print ('Outubro')
    elif mes == '11':
        print ('Novembro')
    elif mes == '12':
        print ('Dezembro')
    else:
        print ('O número não corresponde a um mês do ano.')
else:
    print ('ATENÇÃO: O valor digitado não é uma data.')

# 18_Faça um algoritmo que valide uma data. A mesma deve ser formada por dia, mês e ano. Por exemplo, se o usuário digitar a data 10/8 a mesma será inválida. Porém, caso a data seja 01/10/2018, a mesma deve ser considerada válida.
data = input('Digite uma data no formatao dd/mm/aaaa: ')
if len(data) == 10:
    if data[2] == '/' and data[5] == '/':
        dia_intervalo = (data[0] + data[1])
        mes_intervalo = (data[3] + data[4])
        ano_intervalo = (data[6] + data[7] + data[8] + data[9])

        if dia_intervalo.isnumeric() == True and mes_intervalo.isnumeric() == True and ano_intervalo.isnumeric() == True:
            numdia = int(dia_intervalo)
            nummes = int(mes_intervalo)
            numano = int(ano_intervalo)

            if numano > 0:
                if nummes > 0 and nummes <= 12:
                    if numdia > 0 and numdia <= 31:
                        print ('Data %s validada com sucesso!' % (data))

                    else:
                        print('O valor digitado não é valido para o formato de data.')
                else:
                    print('O valor digitado não é valido para o formato de data.')
            else:
                print('O valor digitado não é valido para o formato de data.')
        else:
            print('O valor digitado não é valido para o formato de data.')
    else:
        print('O valor digitado não é valido para o formato de data.')
else:
    print('O valor digitado não é valido para o formato de data.')
