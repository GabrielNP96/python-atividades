'''
 Cálculo do Fatorial:

    Entrada: Um número inteiro não negativo.
    Processamento: Utilizar um laço para multiplicar todos os números de 1 até o número fornecido.
    Saída: O fatorial do número.
'''

def factorial():
    try:
        get_user_number = int(input('Digite um número inteiro maior que zero: '))
        if get_user_number > 0:
            factorial = 1
            i = 1
            while i <= get_user_number:
                factorial *= i
                i += 1
            return print(f'O Fatorial de {get_user_number} é {factorial}')
        else:
            return print('Digite apenas números inteiros maiores que zero.')

    except:
        return print('Digite apenas números inteiros maiores que zero.')
    
factorial()