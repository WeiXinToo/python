item1 = 'Phone'
item1_price = 100
item1_quantity = 5
item1_price_total = item1_price * item1_quantity

"""Check for data type"""
print(type(item1)) # str
print(type(item1_price)) # int
print(type(item1_quantity)) # int
print(type(item1_price_total)) # int

"""
- Everything in Python is object.
- "Phone", 100, 5, etcs. are instances that are instantiated from some class (e.g., str/ int/ etc.).
- we can create our own data type to be reused in the future.
- each instance would have attributes that store information.
"""