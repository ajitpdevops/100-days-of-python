from item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0) -> None:
        super().__init__(name, price, quantity)

        assert broken_phones >= 0, f"Broken phone quantity {broken_phones} is less than 0"
        assert broken_phones <= quantity, f"Broken phones quantiry {broken_phones} is greater than the actual quantity {quantity}"

        self.broken_phones = broken_phones
        

    def sellable_quantity(self):
        return self.quantity - self.broken_phones
