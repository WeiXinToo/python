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
    return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

  def calculate_total_price(self):
    return self.price * self.quantity
  
  def apply_discount(self):
    self.price = self.price * self.pay_rate 
  
  @classmethod
  def instantiate_from_csv(cls):
    
    with open(r"C:\Users\Wei Xin\Desktop\Web\Python\OOP\csv\6. items.csv", "r") as file:
      reader = csv.DictReader(file)
      items = list(reader)
    
    for item in items:
      Item(
        name=item.get('name'),
        price=float(item.get('price')),
        quantity=int(item.get('quantity')),
      )

"""Phone
- can't create method related to phone in class Item.
- don't have phone related attributes.
- Most importantly, creating these methods and properties have no use for other Items that is not phone per se.
- Solution: Inheritance!
"""
class Phone(Item):
  """
  class child(parent):
    ...
  """
  def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
    
    # Call to super function to have access to all attributes/ methods
    """call init() in parent class"""
    super().__init__(
      name, price, quantity
    )

    # Run validations to the received arguments
    assert price >= 0, f"Price {price} is not greater than or equal to zero!"
    assert quantity >= 0, f"Price {quantity} is not greater than or equal to zero!" 
    assert broken_phones >= 0, f"Price {broken_phones} is not greater than or equal to zero!" 


    # Assign instance attributes to each instance (self) 
    
    self.broken_phones = broken_phones



phone1 = Phone("jscPhonev10", 500, 5, 1)
print(phone1.calculate_total_price())
phone2 = Phone("jscPhonev20", 700, 5, 1)


"""
phone1 = Item("jscPhonev10", 500, 5)
phone1.brooken_phones = 1
phone2 = Item("jscPhonev20", 700, 5)
phone2.broken_phones = 1
No error!
"""

print(Item.all)
print(Phone.all)