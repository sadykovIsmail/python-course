

class Category:
    
    
    def __init__(self, ledger):
        self.ledger = ledger
        self.ledger = []
        
    
    def deposit(self, amount, description=""):
        
        self.ledger.append({'amount': amount, 'description': description})
        # return print(self.ledger)

    def withdraw(self, amount, description=""):
    # Calculate current balance
        balance = sum(item["amount"] for item in self.ledger)

    # If not enough money → return False
        if amount > balance:
            return False

    # Otherwise add a withdrawal entry (negative amount)
        self.ledger.append({"amount": -amount, "description": description})
        return True

        
        
        
        
def create_spend_chart(categories):
    pass

hello = Category(0)
hello.deposit(35)
hello.withdraw(3)
print(hello.ledger)
# hello.withdraw(30)




