programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
}

# print(programming_dictionary)

## Retrive / Add / Edit the item in dict

# print(programming_dictionary["Bug"])

# programming_dictionary["Loop"] = "The action of doing something over and over again."

# programming_dictionary["Bug"] = "A moth in your computer."

# print(programming_dictionary["Bug"])

## Loop through the dict 

# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])


#######################################

#Nesting 
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

# Nesting a List in a Dictionary

travel_log = {
    "France": { "cities_visited": ["Paris", "Lille", "Dijon"], 
                "number_of_visits": 12,
                "cities_on_list": ["Lyon", "Marseille"], },
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}


# Nesting Dictionaries in Lists

travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]

# Write a function will add a new item in the travel_log
def add_new_country(country_name, visits_count, list_of_cities):
    new_dict = {}
    new_dict["country"] = country_name
    new_dict["cities_visited"] = list_of_cities
    new_dict["total_visits"] = visits_count
    travel_log.append(new_dict)


# call the function
add_new_country("Russia", 2, ["Moscow", "Saint Peris"])
#print(travel_log)


starting_dictionary = {
    "a": 9,
    "b": 8,
}

starting_dictionary["c"]=7
final_dictionary = starting_dictionary

print(final_dictionary)

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order["main"][2][0])