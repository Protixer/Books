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

# valorant_agents = {"duelist": "Jet", "controller": "Viper", "Sentinel": "Kill Joy"}
#
# for key, value in valorant_agents.items():
#     print(f"{key}: {value}")
#     print(f"{key}")
#     print(f"{value}")


# def get_most_common_enemy(enemies_dict):
#     max_so_far = float("-inf")
#     most_common = None
#     for enemy_name in enemies_dict:
#         count = enemies_dict[enemy_name]
#         if count > max_so_far:
#             max_so_far = count
#             most_common = enemy_name
#     return most_common
#
#
# get_most_common_enemy({"jackal": 4, "kobold": 3, "soldier": 10, "gremlin": 5})


# def count_vowels(text):
#     list = []
#     for char in text:
#         tolower_char = char.lower()
#         if tolower_char in "aeiou":
#             list.append(char)
#
#     count_values = len(list)
#     unique_values = set(list)
#     return count_values, unique_values
#
#
# count_vowels("Did someone say Thunderfury, Blessed Blade of the Windseeker?")


# my_dict = {"duelist": "Jet", "smoker": "Omen"}
#
# for key, value in my_dict.items():
#     print(f"{key}: {value}")
#
# my_dict["duelists"] = my_dict["duelist"]
# del my_dict["duelist"]
#
# for agent in my_dict.values():
#     print(agent)
#
# for key in my_dict.keys():
#     print(f"{key}: {my_dict[key]}")

# favorite_languages = {
#     "jen": "python",
#     "sarah": "c",
#     "edward": "rust",
#     "phil": "python",
# }
# friends = ["phil", "sarah"]
# for name in favorite_languages.keys():
#     print(f"Hi {name.title()}!")
#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"{name.title()} is {language.title()}")
