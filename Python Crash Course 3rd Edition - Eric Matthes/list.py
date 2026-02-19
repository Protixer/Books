# valorant_agents = ['Jett', 'Sage', 'Raze', 'Breach', 'Omen', 'chamber']

# print(valorant_agents)
# print(valorant_agents[0])
# print(valorant_agents[1:4])
# print(valorant_agents[-1])
# print(valorant_agents[-2])
# print(f'Best valorant agent is {valorant_agents[-1].title()}')
#
# valorant_agents[1] = 'Reyna'
# print(valorant_agents)
#
# for agent in valorant_agents:
#     print(agent.title())
#
# valorant_agents.append('Sky')
# print(valorant_agents)
#
# valorant_agents.insert(0, 'Viper')
# print(valorant_agents)

# Sorted does not change the original list, it returns a new sorted list
# sorted_valorant_agents = sorted(valorant_agents)
# print(valorant_agents)
# print(sorted_valorant_agents)
# print(valorant_agents)

# # Sort method changes the original list
# sort_valorant_agents = valorant_agents.sort()
# print(valorant_agents.sort())
# print(sort_valorant_agents)
# print(valorant_agents)

# Reverse method changes the original list
# numbers = [1, 2, 3, 4, 5]
# numbers.sort(key=lambda x: x,reverse=True)
# print(numbers)
# print(len(numbers))
# numbers.reverse()
# print(numbers)

# for agent in valorant_agents[0:2]:
#     print(agent)

# for agent in valorant_agents[::2]:
#     print(agent)

# for agent in valorant_agents:
#     print(f"Hello, {agent.title()}!")
#
# print(f"Hello, {agent.title()}!")
#
# squares = [value**2 for value in range(1,11)]
# print(squares)

# print(valorant_agents[0:3])
# print(valorant_agents[4:])

# my_foods = ['pizza','falafel','carrot cake']
# simona_foods = my_foods[:]
# my_foods.append('chicken')
# simona_foods.append('chips')
# simona_foods.append('ice cream')
#
# print("My favorite foods are:")
# print(my_foods)
#
# print("Simona's favorite foods are:")
# print(simona_foods)

my_foods = ['pizza','falafel','carrot cake']
simona_foods = my_foods
simona_foods.append('chips')
my_foods.append('chicken')
simona_foods.append('ice cream')
print(my_foods)
print(simona_foods)