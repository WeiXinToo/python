class Item:
  def calculate_total_price(self, x, y):
    """method always receive self as its first argumenet
    refer to current object
    """
    return x * y



"""
Creating instance of our own class.
It is similar to how we create strings.
random_str = str("4")
random_str = "4"


Q: Why creating built-in data type, we don't put str() or int() when creating them?
A: ??? 
"""

# create an instance of the class Item
item1 = Item() 
# add/ assign/ create attribute to instances of class 
item1.name = "Phone"
item1.price = 100
item1.quantity = 5

# create second instance
item2 = Item()
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3
"""
Q: Difference between item1.name = "Phone" vs name = "Phone"?
A: One (instance variable) related to object, one doesn't.

P: For each item we create, We need to manually assign attributes for them/ hard code in the attribute name.
Q: How can we create an instance with attributes built-in?
A: __init__() initialization method
"""

random_str = "aaa"
print(random_str.upper()) # method for instance to turn them into uppercase.
"""
Q: How can we design method for instance?
A: Method refers to function belong to class.
"""


"""
Assessing method by instance using dot.
Python always passes instance e.g., item1/ item2 as its first argument of the method, then item1.price and item1.quantity
"""
print(item1.calculate_total_price(item1.price, item1.quantity))
print(item2.calculate_total_price(item2.price, item2.quantity))

"""Check types"""
print(type(item1)) # __main__.Item
print(type(item1.name)) # str
print(type(item1.price)) # int
print(type(item1.quantity)) # int