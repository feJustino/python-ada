idade = int(input("Qual sua idade? "))

if idade >= 18:
  print("você é maior de idade")
else:
  print("você é menor de idade")

nota = float(input("Qual sua nota? "))
presenca = int(input("Qual sua presença? "))

if nota >= 7:
  print("Aprovada(o)")
elif nota >= 5:
  print("Recuperação")
else:
  print("Reprovada(o)")

if nota >= 7 and presenca < 70:
  print("Aprovada(o)")
else:
  print("Reprovada(o)")