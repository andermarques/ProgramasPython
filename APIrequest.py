#Uma API que faz requisições


import requests
url = ' https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'
valor = requests.get(url)
valor = valor.json()
dolar = valor['USDBRL']['bid']
euro  = valor['EURBRL']['bid']
reais = float(input('Informe o valor em reais(R$) a ser convertido: '))
dolares = reais/float(dolar)
euros = reais/float(euro)
print(f'O Valor convertido vale {dolares:.2f} dolares')
print(f'O Valor convertido vale {euros:.2f} euros')







