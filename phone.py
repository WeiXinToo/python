from item import Item

class Phone(Item):

  pay_rate = 0.5
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
