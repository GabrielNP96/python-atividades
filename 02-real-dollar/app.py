'''
Conversão de Moedas:

    Entrada: Valor em real.
    Processamento: Multiplicar o valor pela taxa de conversão para dólar.
    Saída: Valor convertido.
'''

def real_to_dollar():
    try:
        getReal = float(input('Digite o valor em Reais: '))
        return print(f'${getReal} convertido para dólar é igual a ${getReal * 5.64}')
    except:
        print('Você deve digitar apenas um número.')
real_to_dollar()