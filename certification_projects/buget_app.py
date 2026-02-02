
class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = []

  def deposit(self, amount, description=''):
    self.ledger.append({'amount': amount, 'description': description })

  def withdraw(self, amount, description=''):
    if self.check_funds(amount):
      self.ledger.append({'amount' : -amount, 'description': description})
      return True
    else:
      return False
  def get_balance(self):
    balance = 0
    for dict in self.ledger:
      balance += dict['amount']
    return balance


    
  
  def transfer(self, amount, destination):
    if self.check_funds(amount):
      self.withdraw(amount, f'Transfer to {destination.name}')
      destination.deposit(amount, f'Transfer from {self.name}')
      return True
    return False

  def check_funds(self, amount):
    balance = self.get_balance()
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
    transaction_history = ''
    total = 0
    for transaction in self.ledger:
      description = transaction['description'][:23]
      amount = f"{transaction['amount']:.2f}"[:7]
      total += transaction['amount']
      transaction_history += f"\n{description}{' '*((23 - len(description))+(7-len(amount)))}{amount}"

    transaction_history += f"\nTotal: {total}"

    return title + transaction_history

# food = Category('Food')
# food.deposit(900, 'deposit')
# food.withdraw(45.67, 'milk, cereal, eggs, bacon, bread')
# clothing = Category('Clothing')
# food.transfer(50, clothing)
# clothing.withdraw(15.89, 'T-shirt')
# print(food)

def create_spend_chart(categories):
  title = "Percentage spent by category\n"
  total_spent = 0
  category_total_spent =[]
  longest_category_name = ''
  for category in categories:
    category_spent = 0
    if len(category.name) >= len(longest_category_name):
      longest_category_name = category.name
    for transaction in category.ledger:
      if transaction['amount'] < 0:
        category_spent += abs(transaction['amount'])
        total_spent += abs(transaction['amount'])
    category_total_spent.append({'name': category.name, 'spent_amount': category_spent})
  
  for dictionary in category_total_spent:
    percentage = (dictionary['spent_amount']/total_spent) * 100
    dictionary['percentage'] = int((percentage // 10) * 10)

  for num in range(100,-10, -10):
    if(num < 100 and num > 0):
      title += f" {str(num)}| "
    elif(num == 0):
      title += f"  {str(num)}| "
    else:
      title += f"{str(num)}| "
    for spent_history in category_total_spent:
      if num <= spent_history['percentage']:
        title += 'o  '
      else:
        title += "   "
    title += "\n"
    
  title += f"{' '*4}{'-'}{'-'*(len(categories)*2)}{'-'*2}"
  title += '\n'
  index = 0
  while index < len(longest_category_name):
    title += f"{' '*5}"
    for category in categories:
      if index <= (len(category.name) - 1):
        title += f"{category.name[index]}  "
      else:
        title += "   "
    title += "\n"
    index += 1
  
  return title
  
# create_spend_chart([food, clothing])
