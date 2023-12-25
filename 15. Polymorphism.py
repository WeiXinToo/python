"""
Polymorphism 
- poly: many; morph: form -> many form
- a term being implemented in different areas in whole python programming language.
- refers to use of single type entity (e.g., function) to represent different type in different scenario.

Good example: len() built-in function - show polymorphism - a single entity(function) know how to handle different kinds of objects (str, list, etc) as expected

name = "Jim" # str
print(len(name))

some_list = ["some", "name"] # list
print(len(some_list))


"""
from phone import Phone
from keyboard import Keyboard

item1 = Keyboard("jscKeyboard", 1000, 3)

item1.apply_discount() # displaying polymorphism - we can use this apply_discount() function from different kinds of object and it will know how to handle it properly.

""" 
we can have control of how many amount of discount we want to apply inside our classes

In each child classes, we can override parent discount_rate by assigning class attribute in child classes.

Thus, we have more control.

"""

print(item1.price)
