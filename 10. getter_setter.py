from item import Item

item1 = Item("MyItem", 750)
"""
with @property - _ or __ (read-only mode)

print(item1._Item__name) # read (Note: __ still can be accessed by this way)
print(item1.name) # read
print(item1._name) # Attribute error
print(item1.__name) # Attribute error"""


"""
With @xxx.setter
you can set the value of an instance variable from outside the class

"""
item1.name = "OtherItem123"
print(item1.name)


"""
Mechanisms:
when you use @property on the instance attribute, and then try to access the attribute
e.g., print(item.xxx) or print(item) --item = Item(xxx, yyy, zzz) anything involves xxx the following code will be executed.

@property
def xxx(self):
  return self.__xxx

**********
  
whenevr you use @xxx.setter, and trying to set a value
e.g., item1.xxx = "yyy" the following code will be executed.
@xxx.setter
def xxx(self, value):
  self.__xxx = value


"""