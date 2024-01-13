# Object Oriented Programming with Python

1. Class - A class is blueprint 
2. Object - Object is an instance of a class 

## Class and Objects :
- __init__ : The init method allows us to initialize the attributes or properties of an object/instance when it is being created. It is a special method in Python classes that is called at the instantiation of the class and is used to set up the initial state of an object. [2] 
- assert : The assert statement in Python is used to check for conditions in your code. It allows you to validate whether something is True during the execution of your program
- __repr__ : This method decides the string representation of the instances.
- __dict__ : The 'dict' attribute returns the dictionary containing the class's namespace. This is where normal attributes (like variables, methods etc.) are stored.
- @classmethod : The @classmethod decorator in Python is used to define class methods. Class methods receive the class as the implicit first argument instead of an instance of the class. This allows class methods to access and modify class state without needing an instance of the class.
- @staticmethod - These are utility function that has some relationship with class but not depend on each isntance. 

So in summary - use a class method when you need access to the class or to modify class state, and a static method when the method only depends on parameters rather than the class itself. Let me know if any part of the difference needs more clarification!



## Errors 
- AttributeError: can't set attribute 
- RecursionError: maximum recursion depth exceeded
