menu = """
[D] Depositar
[S] Sacar
[E] Extrato
[F] Fechar

=> """

LIMIT_WITHDRAWAL = 500.00
DAILY_WITHDRAWAL_LIMITS = 3

bank_infos = {
    'balance': 0,
    'withdrawals_made': 0,
    'deposits': [],
    'withdrawals': []
}

def deposit():
    value = float(input('Informe um valor para o depósito: '))

    if value <= 0:
        print('Informe um valor válido')
        return

    bank_infos["deposits"].append(value)
    bank_infos['balance'] += value

def withdraw():
    value = float(input('Informe um valor para o saque: '))

    if bank_infos['withdrawals_made'] >= DAILY_WITHDRAWAL_LIMITS:
        print('Você excedeu os 3 saques diários!')
        return
    
    if value > bank_infos['balance']:
        print('Você não tem esse saldo na conta!')
        return
    
    if value > LIMIT_WITHDRAWAL:
        print('Você não pode sacar mais de R$ 500.00 por saque!')
        return
    
    bank_infos['withdrawals_made'] += 1
    bank_infos['withdrawals'].append(value)
    bank_infos['balance'] -= value

options = {
    'D': deposit,
    'S': withdraw,
}

while True:
    option = input(menu)

    if option.upper() == 'F':
        break

    options.get(option.upper())()


