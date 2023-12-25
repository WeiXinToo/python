class CustomizedInteger:
  def __init__(self, integer):
    self.integer = integer
  
  def __str__(self):
    """
    Informal/ nicely printable string representation of an object.
    No expectation that it will return a valid Python expression.
    User-friendly. 
    """
    if self.integer == 4:
      return "Four"

  def __repr__(self):
    """
    Best practice: valid Python expression that could be used to recreate an object with the same value.
    
    represent object/ instance we created (information rich & unambiguous)

    debugging purpose.
    Machine-friendly/ for programmers.
    """
    return f'CustomizedInteger({self.integer})'

int1 = CustomizedInteger(4)  # __repr__() should represents this Python expression
print(str(int1)) # Four
print(repr(int1)) # CustomizedInteger(4)
print(int1) # Four

"""
Note: In Command Prompt:

>>> str(int1) 
"Four"
>>> int1
CustomizedInteger(4)

"""

