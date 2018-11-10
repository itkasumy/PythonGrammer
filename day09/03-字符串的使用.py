string = 'everything in the world is about sex, Except sex, Sex is about power.'

# find
print(string.find('sex'))
print(string.find('sex', 34, -1))

# index
print(string.index('in'))
# print(string.index('In'))

# count
print(string.count('sex'))

# replace
print(string.replace('about', 'ABOUT', -1))

# split
print(string.split(' '))
print(string.split(' ', 2))

# capitalize
print(string.capitalize())

# title
print(string.title())

# startswith
print(string.startswith('everything'))

# endswith
print(string.endswith('power'))

# lower
print(string.lower())

# upper
print(string.upper())

# ljust
print(string.ljust(120))

# rjust
print(string.rjust(120))

# center
print(string.center(120))

# lstrip
print(string.lstrip())

# rstrip
print(string.rstrip())

# strip
print(string.strip())

# rfind
print(string.rfind('sex'))

# rindex
print(string.rindex('o'))

# partition
print(string.partition('sex'))

# rpartition
print(string.rpartition('sex'))

# splitlines
print(string.splitlines())

# isalpha
print(string.isalpha())

# isdigit
print('123'.isdigit())

# isalnum
print(string.isalnum())

# isspace
print(string.isspace())

# join
ls = ['aa', 'bb', 'cc']
print('-'.join(ls))
