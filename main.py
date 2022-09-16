import requests
from currencies import Currencies


HOST = 'https://www.frankfurter.app/'

def main():
    try:
        available_currencies = requests.get(f'{HOST}/currencies').json()
    except:
        print('Server Error!')
        return

    currencies = Currencies(available_currencies=available_currencies)
    while True:
        action = set_action_grub()
        if action == 's':
            currencies.show_currencies()
            pause()
        elif action == 'c':
            from_currency, to_currency = currencies.get_user_input_currencies()
            amount = float(input('Amount -> '))

            conversion(amount=amount, from_currency=from_currency, to_currency=to_currency)
            pause()
        elif action == 'q':
            break


def set_action_grub():
    while True:
        action = input('\nPress:\n'
                    '   s - Show currencies available\n'
                    '   c - Conversion\n'
                    '   q - Quit\n'
                    '>> ').lower()

        if action in ('s', 'c', 'q'):
            return action
        print('\nInvalid answer!')


def conversion(amount, from_currency, to_currency):
    response = requests.get(f'{HOST}/latest?amount={amount}&from={from_currency}&to={to_currency}').json()
    rates = response['rates']
    result =  tuple(rates.values())[0]
    print(f'{amount} {from_currency} = {result} {to_currency}')


def pause():
    input("\nPress any key to continue...")

if __name__ == '__main__':
    main()