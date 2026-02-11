word_one = 'I like '
word_two = 'you'
full_string = word_one + word_two
print(full_string)
full_string = word_one.strip() + word_two
print(full_string)

# remove prefixes
url = 'https://www.test.com'
print(url.strip('https://'))
print(url.removeprefix('https://'))