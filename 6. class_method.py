import csv

class Item:

  pay_rate = 0.8
  all = []

  def __init__(self, name: str, price: float, quantity=0):
    
    # Run validations to the received arguments
    assert price >= 0, f"Price {price} is not greater than or equal to zero!"
    assert quantity >= 0, f"Price {quantity} is not greater than or equal to zero!" 

    # Assign instance attributes to each instance (self) 
    self.name = name
    self.price = price
    self.quantity = quantity
    
    # Actions to execute
    Item.all.append(self)

  def __repr__(self):
    return f"Item('{self.name}', {self.price}, {self.quantity})"

  def calculate_total_price(self):
    return self.price * self.quantity
  
  def apply_discount(self):
    self.price = self.price * self.pay_rate 
  
  @classmethod
  def instantiate_from_csv(cls):
    """
    class method - class object itself is passed as the first argument in the background
    
    This class method reads the csv file, and instantiate objects.

    """
    with open(r"C:\Users\Wei Xin\Desktop\Web\Python\OOP\csv\6. items.csv", "r") as file:
      reader = csv.DictReader(file)
      items = list(reader)
    
    for item in items:
      Item(
        name=item.get('name'),
        price=float(item.get('price')),
        quantity=int(item.get('quantity')),
      )

Item.instantiate_from_csv()
print(Item.all)

"""
Q: how can I access each instance?
A:
item1 = all[0]
item2 = all[1]?

Q: If we have thousands of instance, how can we access it easily?
"""