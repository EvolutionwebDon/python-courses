# iterating strings
print('--------primeiro exemplo-------')
s = 'iterando strings'
indice = 0

while indice < len(s):
    print(indice, s[indice])
    indice+= 1
#===========================================
print("------------segundo exemplo-------------")
#===========================================
for k,v in enumerate('iterando strings'):
    print(k,v)

print("-----funcoes dos dicionarios------")

tel = {}
tel2 = {
    9999999: "eu",
    88888888: "vc",
    77777777: "tu"
}
tel = {

99422212: "bruno",
99422213: "juliana",
99422214: "fernando"
}
print("RODANDO TUDO")
print(tel)
print("PEGANDO VALOR TOTAL DO DIC USANDO 'len()'")
print(len(tel))
print("PEGANDO O VALOR DA KEY USANDO '.get()'")
print(tel.get(99422212))
print("======================================================")
print(" MOSTRANDO NOVO DICIONARIO")
print(tel2)
print("=======================================================")
print("AGORA ADICIONANDO OS VALORES DE 'TEL2' DENTRO DE 'TEL' DICIONARIO")
tel.update(tel2)
print(tel)
print("==========================================================")
print("ADICIONANDO UMA TUPLA DENTRO D DICIONARIO")
t = (66666666)
tel[t] = "novo contato"
print(tel)
print("===============================================================")
print("AGORA TRABALHANDO COM FUNCOES")
print("====================login=====================")
print(" TRABALHANDO COM LOGIN CHAMANDO FUNCOES COM SENHA")
print()


def login(usuario="root", senha="123"):
    print("Usuario : root")
    print("Senha : 123")





def dados_pessoais(Nome, Sobrenome, Idade, Sexo):
    print("Nome : {}\nSobrenome :{}\nIdade :{}\nSexo :{}".format(Nome, Sobrenome, Idade, Sexo))



while True:
    dados = input("digite sua senha para ver suas informacoes :")
    senha = "123"
    if senha in dados:
        print("--------------------------------")
        print(dados_pessoais("Bruno", "Roberto", 34, "Homen"))
        print("---------------------------------")
        break
    else:
       print("===================SENHA INCORRETA=====================")

def potencia(x):
    quadrado = x**2
    cubo = x**3

    return quadrado, cubo
q,c = potencia(10)

print(q)
print(c)
#=============================================
print("=======================================")
print("=============DESENPACOTANDO DICIONARIO LISTA E TUPLA===========")

def lista_argumento(*lista):
    print(lista)

def lista_association(**dicionario):
    print(dicionario)

lista_argumento(2,1,2)
lista_argumento("hello", "hello1", "hello2")
lista_association(a=1, b=2, c=3)
lista_association(hello=1, hello1=2, hello2=3)

def pessoa(nome, sobrenome, idade):
    print(nome)
    print(sobrenome)
    print(idade)
#tupla = "bruno roberto", "galvao leite", 34
#pessoa(tupla[0], tupla[1], tupla[2])
#pessoa(*tupla)
dic = {"nome":"Bruno roberto", "sobrenome":"galvao leite", "idade":34}
pessoa(**dic)

#==============================================================
lista = [11, 10, 12]

def pacote(a, b, c):
    print(a)
    print(b)
    print(c)
#lista.sort() mostra lista em ordem
#lista.sort()

#pacote(*lista)
# l = [*tupla]
# l.sort()
#pacote(*l)
pacote(**dict(zip(("b", "a", "c"), lista)))
print("=============FIM DO DESEPACOTAMENTO===========")
#==================funcao interna e externa================
def func_externa():
    print("func_externa")

    def func_interna():
        print("func_interna")
    func_interna()
func_externa()

print("===============INSTRUCOES NONLOCAL=====================")

def func_externa2():

    local = 10
    def func_interna1():
        nonlocal local
        local += 1
        print(local)

    func_interna1()
func_externa2()
print("============INSTRUCOES GLOBAL==============================")
x = 10
def new_func():
    global x
    return x
print(new_func())
print("=========================FUNCTION USING PASS PRA CONTINUAR ========================================")
def func_pass():
    pass
func_pass()
print()
print("========================= ========================================")



print("==================================================")