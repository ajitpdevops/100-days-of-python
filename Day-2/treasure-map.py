row1 = ["😃", "🌝", "🌞"]
row2 = ["🐶", "😗", "🐲"]
row3 = ["👍", "🐱", "🤣"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

place = input("Enter a place you want start to hunt? E.g. 11 or 12 oe 23: ")
row = int(place[0]) - 1 
column = int(place[1]) - 1

map[row][column] = 'x'
print(f"{row1}\n{row2}\n{row3}")


