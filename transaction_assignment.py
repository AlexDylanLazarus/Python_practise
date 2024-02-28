class transactions:
    def __init__(self, id, date, type, amount):
        self.id = id
        self.date = date
        self.type = type
        self.amount = amount


trans = {
    "first=transactions": [transactions(1, "29 Feb", "withdraw", 2000)],
    "second": [transactions(2, "1 Mar", "deposit", 6000)],
    "third": [transactions(3, "3 Mar", "deposit", 7000)],
}

print(" #  id   Date       Type     Amount  ")

for key, value in trans.items():
    for i, transaction in enumerate(value, start=1):
        print(
            f" {i}. {transaction.id}  {transaction.date}   {transaction.type}       {transaction.amount}"
        )
