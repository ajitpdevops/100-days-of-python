import csv 

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = [] # List to store all instances of the class Item.

    def __init__(self, name: str, price: float, quantity=0) -> None:
        # Run validations to the received arguments 
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        # Assign to self object
        self.__name = name # __ shows a private attibute
        self.__price = price
        self.quantity = quantity

        # append all instances to the all list
        Item.all.append(self)


    @property
    # Property Decorator = Read-Only Attribute
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        # self.__name = value
        # You can done some more complex validation before allowing your users to set the value. 
        # E.g. Check if the name is not more than 10 charactors log
        if len(value) > 10:
            raise Exception ("value can't be longer than 10 characters")
        else:
            self.__name = value

    @property
    def price(self):
        return self.__price
    
    def increament_value(self, increament):
        self.__price = self.__price + self.__price * increament
        return self.__price
    
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate
        return self.__price
    
    def calculate_total_price(self):
        return self.__price * self.quantity

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
        
    def __connect(self, SMTP_server):
        pass 

    def __prepare_body(self):
        return f"""
        Hello Someone, 

        For product {self.name}, we have {self.quantity} quantities.

        Regards,
        Ajit Patil 
        """
    
    def __send_email(self):
        pass

    def send_email(self):
        # Connect to SMTP Server 
        self.__connect("SMTPHost")
        # Prepare Body
        self.__prepare_body()
        # Send an email 
        self.__send_email()
        print("Email has been sent.")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
    
