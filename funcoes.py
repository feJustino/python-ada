def saudacao():
  print("Seja bem-vinda(o)")
  print("Olá, é um prazer ter você aqui")

def saudacao(nome, local):
    print(f"Seja bem-vinda(o) {nome}")
    print(f"Olá, é um prazer ter você aqui na(o) {local}")


def saudacao(nome, local = "Rua"):
    print(f"Seja bem-vinda(o) {nome}")
    print(f"Olá, é um prazer ter você aqui na(o) {local}")

def soma(num1: int, num2: int):
   return num1+num2
def sub(num1: int, num2: int):
   return num1-num2
def mult(num1: int, num2: int):
   return num1*num2
def div(num1: int, num2: int):
   return num1/num2

def calculadora(num1: int, num2: int, operacao="+"):
  if operacao == "+":
    print("Valor da soma é igual a: ", soma(num1, num2))
  elif operacao == "-":
    print("Valor da subtração é igual a: ", sub(num1, num2))
  elif operacao == "*":
    print("Valor da multiplicação é igual a: ", soma(num1, num2))
  elif operacao == "/":
    print("Valor da divisão é igual a: ", div(num1, num2))

calculadora(10,20)
calculadora(10,20, "-")
calculadora(10,20, "*")