from email import message


class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = []

  def deposit(self, amount, description=''):
    self.ledger.append({'amount': amount, 'description': description })

  def withdraw(self, amount, description=''):
    self.check_funds(amount)
    self.ledger.append({'amount' : -amount, 'description': description})
  
  def transfer(self, amount, destination):
    if self.check_funds(amount):
      self.withdraw(amount, f'Transfer to {destination.name}')
      destination.deposit(amount, f'Transfer from {self.name}')
      return True
    return False

  def check_funds(self, amount):
    balance = 0
    for dict in self.ledger:
      balance += dict['amount']
    if balance < amount or balance == 0:
      return False
    else :
      return True
  
  def __str__(self):
    title = "*" * 30
    midIndex = int(len(title)/2 - len(self.name) / 2)

    first_part_title = title[:midIndex]
    last_part_title = title[midIndex+len(self.name):]
    title = first_part_title + self.name + last_part_title
    transaction_history = ' '*30
    total = 0
    for transaction in self.ledger:
      description = transaction['description'][:23]
      amount = f"{transaction['amount']:.2f}"[:7]
      total += transaction['amount']
      transaction_history += f"\n{description}{" "*(23 - len(description)+(7-len(amount)))}{amount}"
      # 1 .description + 
      # 2. " " till 23 +
      # 3. amount   
      # transaction_history [:23] = description
      # transaction_history [-1:-7] = amount


    transaction_history += f"\nTotal: {total}"

      # if(len(description) < 23):
      #   transaction_history += f"\n{description}{' '*(23 - len(description))}{amount}"
      # else:
      #   transaction_history += f"\n{description}{amount}"
      
    return title + transaction_history

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)

