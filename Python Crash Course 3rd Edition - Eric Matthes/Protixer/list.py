# names = ["Simona","Misho","Oleg","Venci","Toshiqta"]
# mess = f"{names[0]} have good tits!"
# print(mess)

"""Change list values"""
# names = ["Simona","Misho","Oleg","Venci","Toshiqta"]

# for i in range(len(names)):
#     names[i] = input()

# print(f"List:{names}")

"""Add elements to list"""
# names = ["Simona","Misho","Oleg","Venci","Toshiqta"]

# names.append("Gosho")
# names.append("Blzxa")
# names.append("Protixer")

# print(f"List:{names}")

"""Add elements to list"""
# valorant_agents = []

# valorant_agents.append("Jet")
# valorant_agents.append("Reyna")
# valorant_agents.append("Viper")

# print(f"Agents: {valorant_agents}")

"""Add elements to list with insert()"""
# valorant_agents = []

# valorant_agents.insert(0,"Jet")
# valorant_agents.insert(1,"Viper")
# valorant_agents.insert(2,"Reyna")
# valorant_agents.insert(1,"Brim")

# print(valorant_agents)

""" Removing an item using the del Statement"""
# valorant_agents = ["Jet", "Reyna"]
# del valorant_agents[0]
# print(valorant_agents)

""" Removing an Item Using the pop() Method """
# valorant_agents = ["Jet", "Reyna", "Chamber"]
# valorant_agents.pop(1)  # pop() only INDEX
# print(valorant_agents)

# names = ["Simona","Misho","Oleg","Venci","Toshiqta"]
# mess = f"{names[0]} have good tits!"
# print(mess)

"""Change list values"""
# names = ["Simona","Misho","Oleg","Venci","Toshiqta"]

# for i in range(len(names)):
#     names[i] = input()

# print(f"List:{names}")

"""Add elements to list"""
# names = ["Simona","Misho","Oleg","Venci","Toshiqta"]

# names.append("Gosho")
# names.append("Blzxa")

# print(f"List:{names}")

""" Pop() Metod """
# names = ["Simona", "Misho", "Oleg", "Venci", "Toshiqta"]
# names.pop(2)
# print(names)


""" Removing an Item by Value """
# names = ["Simona", "Misho", "Oleg", "Venci", "Toshiqta"]
# names.remove("Misho")
# print(names)


"""Exercise Lists"""

names = ["Supoli", "Bonboni", "Moni", "Simoni"]

for name in names:
    print(f"Come to eat and drink, {name}")

print(f"Sorry, but Supoli will miss event.")
names.remove("Supoli")
names.append("Kracholi")

for name in names:
    print(f"Come to eat and drink, {name}")
