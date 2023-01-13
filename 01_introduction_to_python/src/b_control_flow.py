numbers = [1, 2, 3, 4, 5]
dictionary = {
    "a": "apple",
    "b": "banana",
    "c": "clementine"
}
string = ""

# iterate over a list
for number in numbers:
    print(f'{number} x 5 = {number * 5}') 

# iterate over a dict
for key in dictionary:
    print(f'{dictionary[key]} is stored in {key}')

# pro-tip
for index, number in enumerate(numbers):
    print(f'index: {index}, number: {number}')

while len(string) < 10:
    string = string + "a"
    print(f'{string}')

try:
    f = open('01_introduction_to_python/folder_of_files/names.txt', 'r')
    text = f.read()
    list_of_rows_in_text = text.split('\n')
    for i in list_of_rows_in_text:
        print(f'The name, {i}, appeared in the file')
    f.close()
except:
    print('There was a problem opening the file.')

for number in numbers:
    if number % 2 == 0:
        print(f'{number} is divisible by 2')
    else:
        print(f'{number} is not divisible by 2')
