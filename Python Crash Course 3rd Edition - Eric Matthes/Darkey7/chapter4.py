# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(magician)

# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")
#     print(f"I can't wait to see your next trick, {magician.title()}.\n")
# print("Thank you, everyone. That was a great magic show!")


# 4-1
# pizza_list = ["margarita", "formaggie", "vegetarian"]

# for pizza in pizza_list:
#     print(f"I like {pizza} pizza.")

# print("I really love pizza!!!")


# 4-2
# animals_list = ["cat", "dog", "bunny"]

# for animal in animals_list:
#     print(f"A {animal} would make a great pet.")

# print("Any of these animals would make a great pet!!")


# numbers = list(range(1, 6))
# print(numbers)


# even_numbers = list(range(2, 11, 2))
# print(even_numbers)


# squares = []
# for value in range(1, 11):
#     squares.append(value**2)
# print(squares)


"""LIST COMPREHENSION"""

# squares = [value**2 for value in range(1, 11)]
# print(squares)


# 4-3
# for num in range(1, 21):
#     print(num)


# 4-4 and 4-5
# million_numbers = list(range(1, 1000001))

# print(min(million_numbers))
# print(max(million_numbers))
# print(sum(million_numbers))

# # 4-6
# for odd_num in range(1, 21, 2):
#     print(odd_num)

# 4-7
# for num in range(3, 31):
#     print(num * 3)


# 4-8
# for num in range(1, 11):
#     print(num**3)


# 4-9
# list_of_cubes = [num**3 for num in range(1, 11)]
# print(list_of_cubes)


"""SLICING LISTS"""

# players = ["charles", "martina", "michael", "florence", "eli"]

# print(players[0:3])
# print(players[1:4])
# print(players[:4])
# print(players[2:])
# print(players[-3:])

# print("Here are the first three players on my team:")
# for player in players[:3]:
#     print(player.title())


"""COPYING LISTS"""

# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:] #you can make a slice that includes the entire
# #original list by omitting the first index and the second index to create a copy

# my_foods.append('cannoli')
# friend_foods.append('ice cream')

# print("My favorite foods are:")
# print(my_foods)
# print("\nMy friend's favorite foods are:")
# print(friend_foods)


# 4-10
# players = ["charles", "martina", "michael", "florence", "eli"]
# print(f"The first three items in the list are: {players[:3]}")
# print(f"Three items from the middle of the list are: {players[1:4]}")
# print(f"The last three items in the list are: {players[-3:]}")


# 4-11
# pizza_list = ["margarita", "formaggie", "vegetarian"]
# friend_pizzas = pizza_list[:]

# pizza_list.append("italian")
# friend_pizzas.append("pepperoni")

# print("My favourite pizzas are:")
# for pizza in pizza_list:
#     print(pizza)

# print("My friend's favorite pizzas are:")
# for friend_pizza in friend_pizzas:
#     print(friend_pizza)


"""TUPLES = immutable lists"""

# dimensions = (200, 50)
# print(dimensions[0])
# print(dimensions[1])

# dimensions[0] = 250 # gives an error, because tuples are immutable and their values cannot be changes

"""NOTE!! - Tuples are technically defined by the presence of a comma; the parentheses make them
look neater and more readable. If you want to define a tuple with one element, you
need to include a trailing comma: my_t = (3,)"""

# for dimension in dimensions:
#     print(dimension)

"""OVERWRITING TUPLES"""

# dimensions = (200, 50)
# print("Original dimensions:")
# for dimension in dimensions:
#     print(dimension)

# dimensions = (400, 100)
# print("\nModified dimensions:")
# for dimension in dimensions:
#     print(dimension)


# 4-13
# buffet_menu_tuple = ("milk", "bread", "butter", "jam", "cereal")

# for food in buffet_menu_tuple:
#     print(food)

# buffet_menu_tuple = ("tea", "bread", "eggs", "jam", "cereal")

# for food in buffet_menu_tuple:
#     print(food)
