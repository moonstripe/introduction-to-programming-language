# Nothing to import

# strings, integers, floats, booleans

# strings
hello = "hello"
world = "world"
fake_one = "1"

# integers
one = 1
two = 2

# floats
almost_zero = 0.01
almost_one = 0.99
check_coordinate = 35.4736

# booleans
factual = True
fictitious = False

# native_functions
capitalized_hello = hello.capitalize()

# tuples, lists, dicts

# tuple
some_coordinate = (35.4736, 36.8624)
another_coordinate = (102.4381, 26.1265)

# list
programs = ["IEM", "IPD", "NPTS", "TLM", "TESOL", "TI", "ITED", "IEP"]

# dicts
building_reference = {
    "123 Main St": ["John Realname", "Jimmy Realname", "Linda Realname", "Anna Realname"],
    "125 Main St": ["Antonio Truetitle", "Karina Truetitle", "Veronica Truetitle"]
}


if __name__ == "__main__":
    # basic types are the building blocks of meaningful code

    # concatenate strings together
    print(f'Concatinating strings: {hello + " " + world}')

    # adding numbers together:
    print(f'Adding integers: {one + two}')

    # adding floats together:
    print(f'Adding floats: {almost_zero + almost_one}')
    
    # NOTE: issues start arising when we mix types...

    # this line runs as expected:
    print(f'Adding a float to an integer: {one + almost_one}')

    # when uncommented, this line fails:
    # print(f'This printline will not appear due to an error: {hello + one}')

    print(f'New hello world: {capitalized_hello + " " + world}')

    # basic collections are powerful ways to store basic types...

    # NOTE: you cannot add elements to tuples,
    # but you can add to lists and dicts.

    # adding PYTH to list of programs
    programs.append("PYTH")
    print(f'Program list: {programs}')

    # adding a new family to building_reference
    building_reference["127 Main St"] = ["本名和子", "本名智", "本名武"]
    print(f'Building reference: {building_reference}')
    
    # when uncommented, this line fails:
    # fake_coordinate = another_coordinate.append(99.9999)

    # get item at index 0
    print(f'The Latitude of some_coordinate: {some_coordinate[0]}')

    # ...so we can use them later

    # we can "destructure" tuples
    lat, long = another_coordinate

    print(f'another_coordinate, Latitude: {lat}, Longitude: {long}')

    # get element at index 4
    print(f'In list of programs, the program stored at index 4 is {programs[4]}')

    # get index of "IPD" from list
    print(f'In list of programs, "IPD" is stored at index {programs.index("IPD")}')

    # get value from key "123 Main St":
    print(f'The inhabitants of "123 Main St": {building_reference["123 Main St"]}')