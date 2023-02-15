# file = open("./test.txt")
# contents = file.read()
# print(contents)
# file.close()


# with open("./test.txt") as file:
#     contents = file.read()
#     print(contents)


# with open("./test.txt", mode="a") as f:
#     f.write("\nNew text.")


# # "w" mode creates a new file if it's not there. It also overwrites file if there is a content alreay    
# with open("./my_test.txt", mode="w") as f:
#     f.write("New text.")

data = []    
with open("./weather_data.csv") as f:
    line = f.readline()
    for line in f:
        data.append(line)

print(data)    


