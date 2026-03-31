# alien_0 = {'color': 'green',
#            'points': 5 }
#
# print(alien_0['color'])
# print(alien_0['points'])
#
# alien_0 = {'color':'purple'}
# print(alien_0)
# print(alien_0['color'])
#
# alien_0['score'] = 10
# print(alien_0)
# alien_0['points'] = 5
# print(alien_0)
# print(alien_0['points'])
# print(alien_0['score'])
#

# valorant_agents = {}
# valorant_agents['duelist'] = 'Jet'
# valorant_agents['controller'] = 'Brim'
# valorant_agents['sentinel'] = 'Breach'
# print(valorant_agents)
# print(valorant_agents['duelist'])


# for agent in valorant_agents:
#   print(agent)

# valorant_agents = {'duelist': 'Jet', 'controller': 'Viper', 'Sentinel': 'Kill Joy'}
# picked_agent = 'sen'

# # Check if the key exists directly
# if picked_agent in valorant_agents:
#     print(valorant_agents[picked_agent])
# else:
#     # If the key doesn't exist, default to controller
#     picked_agent = 'controller'

valorant_agents = {"duelist": "Jet", "controller": "Viper", "Sentinel": "Kill Joy"}

for key, value in valorant_agents.items():
    print(f"{key}: {value}")
