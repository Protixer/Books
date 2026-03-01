# cars = ["audi", "bmw", "subaru", "toyota"]
#
# for car in cars:
#     if car == "bmw":
#         print(car.upper())
#     else:
#         print(car.lower())
#
#
# reqiested_toppings = ["mushrooms", "extra cheese"]
#
# if "mushrooms" in reqiested_toppings:
#     print("Adding mushrooms.")
# else:
#     print("Adding pepperoni.")
#
# valorant_agent = "Viper"
# if valorant_agent != "Reyna":
#     print(f"Hello, {valorant_agent.title()}!")

# a = 5
# b = 14
# c = 11
#
# if a > b or c > b:
#     print("C is biggest")
# elif a < b and b > c:
#     print("B is biggest")
#
# valorant_agents = ["Jett", "Sage", "Raze", "Breach", "Omen", "chamber"]
# if "Viper" not in valorant_agents:
#     print("You are not a valorant agent")

# car = "subaru"
# print("Is car == 'subaru'? I predict True.")
# print(car == "subaru")
# print("\nIs car == 'audi'? I predict False.")
# print(car == "audi")


age = 12
if age < 4:
    print("Your admission cost is $0")
elif age < 18:
    print("Your admission cost is $50")
elif age < 21:
    print("Your admission cost is $75")
else:
    print("Your admission cost is $100")


age = 12
if age < 4 or age < 18:
    print("Your admission cost is $0")
elif age < 21 or age > 25:
    print("Your admission cost is $75")
