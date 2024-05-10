class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __call__(self):
        print(f"{self.currency} {self.amount}")

    def __repr__(self):
        return str(self.currency)

    def __add__(self, other):
        currency = self.currency[0] + other.currency[1:]
        amount = other.amount
        return Currency(currency, amount)


c1 = Currency("dollar", 5)
c2 = Currency("dollar", 10)
c3 = Currency("shekel", 1)
c4 = Currency("shekel", 10)
c5 = c2 + c4

print(c1.currency)
print(c2.amount)
repr(c3)
print(c5)
print(c1 + 5)
