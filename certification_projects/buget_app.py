class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = []

  def deposit(self, amount, description=''):
    self.ledger.append({'amount': amount, 'description': description })

  def withdraw(self, amount, description=''):
    self.ledger.append({'amount' : -amount, 'description': description})
  
  def transfer(self, amount, destination):
    if self.withdraw(amount, f'Transfer to {destination.name}'):
      return True
    if self.deposit(self, amount, f'Transfer from {self.name}'):
      return True
    return False

  def check_funds(self, amount):
    balance = 0
    # iterate over self.ledger = {amount, description}
    for amt , desc in self.ledger:
      balance += amt
    if balance < amount or balance == 0:
      return False
    else :
      return True