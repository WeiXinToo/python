from item import Item

item1 = Item("MyItem", 750, 6)

"""
Abstraction - only shows necessary attributes and hide unnecessary information from users - who use the class to create objects/instances (like me or other developers).
(to abstract the information that is unnecessary to call it or to access it)


def send_email():
    xxx()
    yyy()
    zzz()

Note: usually we only allow send_email() to be accessible outside of the class, and hide the xxx, yyy, and zzz.


Solution: make some methods private by double underscore
e.g., def __xxx():
        ...
this makes the methods private and only accessible inside class.

item1.connect() # this is not accessible
item1.__connect() # this is also not accessible
"""

item1.send_email()

