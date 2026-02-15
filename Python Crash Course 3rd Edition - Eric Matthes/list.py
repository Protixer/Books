valorant_agents = ['Jett', 'Sage', 'Raze', 'Breach', 'Omen', 'chamber']
print(valorant_agents)
print(valorant_agents[0])
print(valorant_agents[1:4])
print(valorant_agents[-1])
print(valorant_agents[-2])
print(f'Best valorant agent is {valorant_agents[-1].title()}')

valorant_agents[1] = 'Reyna'
print(valorant_agents)

for agent in valorant_agents:
    print(agent.title())

valorant_agents.append('Sky')
print(valorant_agents)