import csv

class Item:

  pay_rate = 0.8
  all = []

  def __init__(self, name: str, price: float, quantity=0):
    
    # Run validations to the received arguments
    assert price >= 0, f"Price {price} is not greater than or equal to zero!"
    assert quantity >= 0, f"Price {quantity} is not greater than or equal to zero!" 

    # Assign instance attributes to each instance (self) 
    """double underscore - """
    self.__name = name
    self.__price = price
    self.quantity = quantity
    
    # Actions to execute
    Item.all.append(self)

  @property
  # Property Decorator = Read-Only Attribute
  def name(self):
    return self.__name
  
  @property
  def price(self):
    return self.__price
  
  def apply_discount(self):
    self.__price = self.__price * self.pay_rate

  def apply_increment(self, increment_value):
    self.__price = self.__price + self.__price * increment_value

  def calculate_total_price(self):
    return self.price * self.quantity

  @name.setter
  def name(self, value):
    if len(value) > 10:
      raise Exception("The name is too long")
    else:
      self.__name = value


  def __repr__(self):
    return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

  def __connect(self, smpt_server):
    pass

  def __prepare_body(self):
    return f"""
    Hello Someone.
    We have {self.name} {self.quantity} times.
    Regards, Wei Xin    

  """
  def __send(self):
    pass 

  def send_email(self):
    self.__connect("")
    self.__prepare_body()
    self.__send()

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

