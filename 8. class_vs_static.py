# When to use class methods and when to use static methods?

def is_integer():
  """
  This should do something that has a relationship with the class, but not something that must be unique per instance!
  """
  ...


class Item:
  @staticmethod
  def is_integer():
    """
    This should do something that has a relationship with the class, but not something that must be unique per instance!
    
    like regular function outside a class

    do not rely on instance / class-specific data

    usage: utility functions, code organization within class
    """
    ...
  
  @classmethod
  def instantiate_from_something(cls):
    """
    e.g, instantiate from json/ csv/ yaml/ string...


    This should also do something that has a relationship with the class, but usually, those are used to manipulate different structures of data to instantiate objects, like we have done with csv.

    allow manipulate class-specific attributes

    usage: accessing class variables, alternate constructor(construct instances of the class in different input format), working with class-specific operations
    """

    """
    Main difference:
    Static method = doesn't take cls as first argument.
    Class method = cls as first argument.
    """


"""
Although instance still can access class methods and static methods, there is no good reason for doing so.
Please don't do it!

"""
item1 = Item()
item1.is_integer(5)
item1.instantiate_from_something()