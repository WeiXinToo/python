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
    
    with open(r"C:\Users\Wei Xin\Desktop\Web\Python\OOP\csv\6. items.csv", "r") as file:
      reader = csv.DictReader(file)
      items = list(reader)
    
    for item in items:
      Item(
        name=item.get('name'),
        price=float(item.get('price')),
        quantity=int(item.get('quantity')),
      )
    
  @staticmethod
  def is_integer(num):
    """
    static method: we never send object/class as the first argument.

    treat it as regular function.

    Q: why do we need @staticmethod? without it, the class can also access this function?

    Q: static method vs regular function

    isinstance(object, type) fx return True if the specific object is of the specified type, otherwise False

    is_integer() - a float method to check for present of fractional part (float), without fractional part(e.g., .0) deems as int
    """
    # We will count out the floats that are point zero
    # For i.e: 5.0, 10.0
    if isinstance(num, float):
      # Count out the floats that are point zero
      return num.is_integer() # check the float has fractional part or not, if not, return True. e.g., 7.0 -> True, 7.5 -> False""
    elif isinstance(num, int):
      return True
    else:
      return False

print(Item.is_integer(7.0)) # True
print(Item.is_integer(7.5)) # False
print(Item.is_integer(7)) # True
print(Item.is_integer("Hello")) # False

