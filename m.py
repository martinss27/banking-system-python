menu = """
[D] Depositar
[S] Sacar
[E] Extrato
[F] Fechar

=> """

balance = 0
bank_statement = {
    'deposit': []
}

def deposit():
    global balance

    value = float(input('Informe um valor para o depósito: '))

    if value <= 0:
        print('Informe um valor válido')
        return

    bank_statement["deposit"].append(value)

    balance += value

options = {
    'D': deposit,
}

while True:
    option = input(menu)

    if option == 'F':
        break

    options.get(option)()


    