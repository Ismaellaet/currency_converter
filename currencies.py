class Currencies:
    def __init__(self, available_currencies) -> None:
        self.available_currencies = available_currencies


    def show_currencies(self):
        for key, value in self.available_currencies.items():
            print(f'{value:24} -> {key:>4}')

    def get_user_input_currencies(self):
        while True:
            from_currency = input('\nFrom currency -> ').upper()
            to_currency = input('To currency -> ').upper()
            currencies_exist = self.validation(from_currency, to_currency)

            if currencies_exist:
                return (from_currency, to_currency)
            print('\nInvalid currencies')


    def validation(self, currency1, currency2):
        return all(currency in self.available_currencies for currency in (currency1, currency2))