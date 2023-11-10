dicionario = {}
dicionario = dict()
Dados_Pessoais = {"Nome": "Felipe", "idade": 23, "altura": 1.77}
print(Dados_Pessoais["Nome"])
Dados_Pessoais["programador"]= True
Dados_Pessoais["altura"] = 1.79

for key in Dados_Pessoais:
  print(key, ":")
  print(Dados_Pessoais[key])


print("valida se chave existe")
print("peso" in Dados_Pessoais)
print("altura" in Dados_Pessoais)