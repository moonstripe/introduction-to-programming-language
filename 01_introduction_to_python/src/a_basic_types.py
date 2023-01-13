# #string or str
# hello = 'hello'
# world = 'world'

# # integer or int
# one = 1
# two = 2

# # float
# almost_zero = 0.01
# almost_one = 0.99

# # boolean
# factual = True
# fictitious = False

# # concatenating strings together
# print(f'Concatenating strings: {hello + " " + world}')

# # adding numbers together
# print(f'Adding integers: {one + two}')

# # adding floats together
# print(f'Adding floats: {almost_one + almost_zero}')

# # adding a float to an integer
# print(f'Adding a float to an integer: {one + almost_one}')

# collections

# tuple
some_coordinate = (35.54736, 36.8624)
another_coordinate = (102.4381, 26.1265)

# list
programs = ["IEM", "IPD", "NPTS", "TLM", "TESOL", "TI", "ITED", "IEP"]

# dicts
building_reference = {
    "123 Main St": ["John Realname", "Jimmy Realname", "Linda Realname", "Anna Realname"],
    "125 Main St": ["Antonio Truetitle", "Karina Truetitle", "Veronica Truetitle"]
}

# we can "destructure" tuples
lat, long = another_coordinate

print(f'another_coordinate, Latitude: {lat}, Longitude: {long}')

# get element at index 4
# NOTE: indices start at 0

print(f'In list of programs, the program stored at index 4 (fifth element) is {programs[2]}')

# get index of "IPD" from list of programs
print(f'In list of programs, "IPD" is stored at index {programs.index("IPD")}')

# get value from key "123 Main St":
print(f'The inhabitants of "123 Main St": {building_reference["123 Main St"]}')

# adding PYTH to list of programs
programs.append("PYTH")
print(f'Program list: {programs}')

# removing the item at index 8
programs.pop(8)
print(f'Program list: {programs}')

# adding a new family to building_reference
building_reference["127 Main St"] = ["本名和子", "本名智", "本名武"]
print(f'Building reference: {building_reference}')