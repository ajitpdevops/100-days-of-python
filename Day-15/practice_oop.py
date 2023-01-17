"""
Class : is a blueprint for an objects you want to create
    E.g. Car
Object: is an instance of a class
    E.g. i20, i10, sonet etc. are the objects created using Car class
Attributes : is something that object has
    E.g. seats - number of seats is an attribute that every car has
Methods : is something that object does
    E.g. move() - Car moves when the method is called
"""



class User:

    # constructor or the initializer
    def __init__(self, user_id, username):
        # print("New object is being created....")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Ajit")
user_2 = User("002", "Anu")
# user_1.id = "001"
# user_1.username = "Ajit"

print(user_1.id, user_2.id)
print(user_1.username, user_2.username)

# when user user_1 follows the user_2
# user_1's following count increases by 1
# user_2's follower count increases by 1

user_1.follow(user_2)
print(f"user_1 followers: {user_1.followers}, user_1 following: {user_1.following}")
print(f"user_2 followers: {user_2.followers}, user_2 following: {user_2.following}")
