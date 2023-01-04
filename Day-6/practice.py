# Function that take argument 

def greet(name):
    print(f"Hello {name}")
    print(f"How are you doing today, {name}?")

greet("Ajit")

# multi argument function
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with("Ajit", "London")

greet_with(location="London", name="Ajit")
