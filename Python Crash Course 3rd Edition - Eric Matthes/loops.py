# cars = ["audi", "bmw", "subaru"]
#
# for car in cars:
#     print(car)


def meditate(mana, max_mana, num_potions):
    current_mana = mana
    maximum_posible_mana = max_mana
    numbers_of_potions = num_potions

    while True:
        if current_mana >= maximum_posible_mana:
            break
        current_mana += 1
        if numbers_of_potions >= 0:
            break
        numbers_of_potions -= 1

    return current_mana, numbers_of_potions


print(meditate(0, 10, 9))
