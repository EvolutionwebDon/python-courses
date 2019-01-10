
acao = str(input("vc gosta de banana?  : "))
acao = str(acao)

if(acao=="sim"):
    print("voce gosta de banana")
    print(40*"-")
else:
    if(acao=="nao"):
       print("voce nao gosta de banana")
       print(40 * "-")
    else:
       print("comer frutas faz bem a saude")
       print(40*"-")
idade = int(input("informe sua idade : "))
if(idade<=17):
    print("voce e de menor!")

    print(40 * "-")
    print("proximo programa")
elif(idade >= 18 ):
    print("voce ja pode transar!!")
    print(40 * "-")
    print("proximo programa")
    print(40 * "-")
else:
    if(idade == 70):
       print("vc ja ta muito velho(a)")

       print(40 * "-")
       print("proximo programa")

#----------------------------------------------------------------

numero1 = input("digite um numero :")
numero1 = int(numero1)

numero2 = input("digite um segundo numero :")
numero2 = int(numero2)

if(numero1==numero2):#operador de igualdade
    print("o numero %d e igual a o numero %d :" % (numero1, numero2))
if (numero1 != numero2):  # operador de diferencia
    print("o numero %d e diferente a o numero %d :" % (numero1, numero2))
if(numero1 > numero2):#operador de maior que
    print("o numero %d e maior que o numero %d :" % (numero1, numero2))
if(numero1 < numero2):#operador de menor que
    print("o numero %d e menor  que o numero %d :" % (numero1, numero2))
#----------------------------------------------------------------------
print(40 * "-")
print("proximo programa")
print(40 * "-")
#----------------------------------------------------------





