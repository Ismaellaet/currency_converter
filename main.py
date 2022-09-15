import requests
from currencies import Currencies


def main():
    host = 'https://www.frankfurter.app/'

    try:
        available_currencies = requests.get(f'{host}/currencies').json()
    except:
        print('Server Error!')
        return

    currencies = Currencies(available_currencies=available_currencies)
    while True:
        action = set_action_grub()
        if action == 's':
            currencies.show_currencies()
            pause = input("\nPress the any key to continue...")
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

if __name__ == '__main__':
    main()