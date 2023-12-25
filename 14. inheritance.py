from phone import Phone

"""
Inheritance - mechanism allows us to reuse codes across all our classes.

Phone class is a child of Item class - inherit all the attributes and methods from parent class.

Parent: Item
Child: Laptop, Phone, etc. anything you can think of.
"""

item1 = Phone("jscPhone", 1000, 3)

item1.apply_increment(0.2)

print(item1.price)