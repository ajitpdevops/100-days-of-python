from item import Item
from phone import Phone

# item1 = Item("Phone", 100, 1)
# item2 = Item("laptop", 100, 3)
# item2.pay_rate = 0.7
# item1.apply_discount()
# item2.apply_discount()
# print(item1.price)
# print(item2.price)
# print(item1)

# print(Item.__dict__)
# print(item1.__dict__)
# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)

# # print(Item.all)
# for instance in Item.all:
#     print(instance.name)

# Item.instantiate_from_csv()
# print(Item.all)

# Topic - Inheritence 
# phone1 = Phone("iPhone14", 599, 20, 1)
# phone2 = Phone("iPhone15", 799)
# # print(Item.all)
# print(Phone.all)
# print(phone1.sellable_quantity())

# Topic - Getter & Setters 


# item1 = Item("MyItem", 25, 1)
# print(item1.name)
# item1.name = "OtherName"
# print(item1.name)

# Topic - Encapsulation 

item1 = Item("MyItem", 30, 1)
# item1.apply_discount()

item1.increament_value(0.2)
print(item1.price)


# Abstraction
# We hide all methods that are used by send_email() method.
item1.send_email()
