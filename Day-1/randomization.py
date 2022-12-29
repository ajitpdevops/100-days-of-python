import random
import my_module

random_integer = random.randint(1, 10)
# print(random_integer)

# print(my_module.pi)

random_float = random.random()
#print(random_float)
print(random_float * 5)


# Flip a coin 

flip = random.randint(0,1)
if flip == 1:
    print("HEADS")
else:
    print("TAILS")

