'''
Cálculo de Imposto de Renda Simples:

Entrada: Renda anual.
Processamento: Aplicar uma alíquota fixa de imposto sobre a renda (por exemplo, 15%).
Saída: Valor do imposto a ser pago.
'''

def simple_tax (income):
    tax = (income / 100) * 15
    return print(f'O valor do imposto de ${income} é ${tax}')

def getIncome():
    income = float(input('Digite sua renda anual: '))
    return income
try:
    simple_tax(getIncome())
except:
    print('Só números são aceitos.')

