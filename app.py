#lista com join que junta as variáveis
campos_endereco = ['Plano Piloto','Asa Sul','SQS 210','Bloco A','Apartamneto 404']

#delimitador separa os nomes com virgula
delimitador = ", "

#junta os valores em uma única variável 
endereco = delimitador.join(campos_endereco)
#exibir variável na tela
print(f"Endereço e carros :{endereco}")

#quando for rodar tem que separar os dois
#--------------------------------------------------------------------------------------------------------

#o split separa as variáveis 
#capitalize é para deixar a letra inicial do nome em letra em maiscula 
#o end= é para evitar quebra de linha como o print faz de forma automatica
nome_completo = input('Informe o seu nome completo: ')

#separar os nomes em uma lista
nome_completo_lista = nome_completo.split(' ')

#capitaliza os nomes e exebe o nome completo na tela 
print('Nome completo: ", end= "')
for nome in nome_completo_lista:
    print(nome.capitalize(), end=" ")
