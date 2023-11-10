import random
print("Bem vindo ao jogo do numero sorteado")
print("Tente adivinhar um numero de 1 a 100")
randomNumber = random.randint(1, 4)
userNumber = int(input("Digite um numero: "))

while randomNumber != userNumber:
  print("você errou tente novamente")
  userNumber = int(input("Digite um numero: "))

print("Parabéns você acertou")

#exemplo 2

contador = 0

while contador < 5:
  print(contador)
  contador = contador + 1