#3-1

# names = ['Ju', "Leo"]

# print(names[0])
# print(names[1])

#3-2

# names = ['Ju', "Leo"]

# print(f'Hello,{names[0]}')
# print(f'Hello,{names[1]}')

#3-3

# transportation = ['car', 'airplane' , 'motorcycle',]

# print(f'I would like to own an Audi {transportation[0]}')
# print(f'I would like to own a Boeing {transportation[1]}')
# print(f'I would like to own an Yamaha {transportation[2]}')


# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# motorcycles.append('ducati')
# print(motorcycles)


# motorcycles = ['honda', 'yamaha', 'suzuki']

# motorcycles.insert(0, 'ducati')
# print(motorcycles)

#DELETE
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# del motorcycles[0]
# print(motorcycles)


#POP()
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)


# motorcycles = ['honda', 'yamaha', 'suzuki']
# last_owned = motorcycles.pop()
# print(f"The last motorcycle I owned was a {last_owned.title()}.")

# motorcycles = ['honda', 'yamaha', 'suzuki']
# first_owned = motorcycles.pop(0)
# print(f"The first motorcycle I owned was a {first_owned.title()}.")


#REMOVE()
# motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# print(motorcycles)
# motorcycles.remove('ducati')
# print(motorcycles)


# motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# print(motorcycles)

# too_expensive = 'ducati'
# motorcycles.remove(too_expensive)
# print(motorcycles)
# print(f"\nA {too_expensive.title()} is too expensive for me.")


#3-4 + 3-5 + 3-6
guests = ['William Shakespeare', 'Stephen Hawking', 'Ryan Reynolds']

print(f'{guests[0]}, you are an incredible writer!')
print(f'{guests[1]}, you are have an outstanding mind!')
print(f'{guests[2]}, you are a great actor!')

print()
print(f'Unfortunately our guest {guests[1]}, won\'t be able to attend')

guests[1] = 'Albert Einstein'

print(f'{guests[0]}, you are an incredible writer!')
print(f'{guests[1]}, you are have an outstanding mind!')
print(f'{guests[2]}, you are a great actor!')

print()
print('Great news everyone, we\'ve found a bigger table, so we will be inviting more guests')

guests.insert(0, "Oprah Winfrey")
guests.insert(2, "Harry Potter")
guests.append('Percy Jackson')

print(guests)

print()
for guest in range(len(guests)):
    print(f'{guests[guest]}, welcome to our dinner party!')

print()
print('Unfortunately we can only have 2 guests over for our dinner party!')

for i in range(len(guests)):
    if i == 4:
        break
    removed_guest = guests.pop()
    print(f'{removed_guest}, you won\'t be able to attend the party!')

print(guests)

for _ in range(len(guests)):
    print(f'{guests[-1]}, you are still invited to the party!')
    del guests[-1]

print()
print(guests)