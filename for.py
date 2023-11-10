
# for variavel in range(10):
#   print(variavel)

# for variavel in range(1,5):
#   print(variavel)

# for variavel in range(1,12, 3):
#   print(variavel)

somaNotas = 0

for i in range(1, 4):
  nota = float(input(f"Informe a sua nota {i}: "))
  somaNotas = somaNotas + nota
print(somaNotas/i)
