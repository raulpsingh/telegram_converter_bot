from currency_converter import CurrencyConverter

currency_converter = CurrencyConverter()


class ConvertCurrenciesAPI:
    amount = None
    currencies = None

    def __init__(self, amount, currencies):
        self.set_data(amount, currencies)

    def set_data(self, amount, currencies):
        self.amount = amount
        self.currencies = currencies

    def convert_currencies(self):
        currencies = self.currencies.split('/')
        result = currency_converter.convert(self.amount, currencies[0], currencies[1])
        return result
