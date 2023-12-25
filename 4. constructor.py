class Item:

  """class attribute - belong to class itself & accessible by instances""" 
  pay_rate = 0.8 # The pay rate after 20% discount

  def __init__(self, name: str, price: float, quantity=0):
    
    # Run validations to the received arguments
    assert price >= 0, f"Price {price} is not greater than or equal to zero!"
    assert quantity >= 0, f"Price {quantity} is not greater than or equal to zero!" 

    # Assign instance attributes to each instance (self) 
    self.name = name
    self.price = price
    self.quantity = quantity
    

  def calculate_total_price(self):
    return self.price * self.quantity
  
  def apply_discount(self):
    """instead of Item.pay_rate, self.pay_rate will look for it in both instance and class level"""
    self.price = self.price * self.pay_rate 


item1 = Item("Phone", 100, 1) 
item2 = Item("Laptop", 1000, 3)

# Class attributes can be accessed by class and instances.
print(Item.pay_rate)
"""when instance couldn't find pay_rate in instance attributes, it will look for it from class level"""
print(item1.pay_rate) 
print(item2.pay_rate)

# __dict__ : a dict obj containing all attributes defined for the object itself.
print(Item.__dict__) # check for attributes in class level
print(item1.__dict__) # check for attribute in instance level 


"""Applying class level attribute vs instance level attribute"""
item1.apply_discount()
print(item1.price)

item2.pay_rate = 0.7 # if laptop have different discount. 
item2.apply_discount()
print(item2.price)


