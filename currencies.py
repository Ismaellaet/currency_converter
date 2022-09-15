class Currencies:
    def __init__(self, available_currencies) -> None:
        self.available_currencies = available_currencies


    def show_currencies(self):
        for key, value in self.available_currencies.items():
            print(f'{value:24} -> {key:>4}')