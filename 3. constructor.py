class Item:
  def __init__(self, name: str, price: float, quantity=0):
    
    """
    magic method/ dunder method.

    constructor - initialize or assign values to the data members/ instance variables of the class when an object of the class is created.

    Note: __new__() is used to create new instance, while __init__() is used to initalize the object's state/ set up the initial attributes or properties of an object when it's created.
    
    add type hint to arguments.
    """
    # Run validations to the received arguments
    assert price >= 0, f"Price {price} is not greater than or equal to zero!"
    assert quantity >= 0, f"Price {quantity} is not greater than or equal to zero!" 

    # Assign instance attributes to each instance (self) 
    self.name = name
    self.price = price
    self.quantity = quantity
    

  def calculate_total_price(self):
    """
    No need to pass other arguments other than self.
    object is passed as argument. 
    instance have access to attribute after initialization.
    """
    return self.price * self.quantity

"""create instance and pass in arguments"""
item1 = Item("Phone", 100, 1) 
item2 = Item("Laptop", 1000, 3)


# call method
print(item1.calculate_total_price())
print(item2.calculate_total_price())

"""we are still allowed to add some more attributes
certain attributes might not be applicable to some items.
"""
item2.has_numpad = False 

