from datetime import datetime

class eplass:
    def __init__(self, amount, category, date):
        self.amount = float(amount)
        self.category = category
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")
    def confirm(self):
        print(f"Expense added: Amount: {self.amount}, Category: {self.category}, Date: {self.date}")
    def display(self):
        print(f"Amount: {self.amount}, Category: {self.category}, Date: {self.date}")
    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "date": self.date
        }
    def displayname(self):
        print(f"{self.category}")