import csv 

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = [] # List to store all instances of the class Item.

    def __init__(self, name: str, price: float, quantity=0) -> None:
        # Run validations to the received arguments 
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # append all instances to the all list
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def check_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


    def __repr__(self) -> str:
        return f"Item('{self.name}', {self.price}, {self.quantity})"
    

    

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
    
Item.instantiate_from_csv()
print(Item.all)