# Nothing to import

# control flow is how we dictate how
# programs operate in certain circumstance

numbers = [1, 2, 3, 4, 5]
dictionary = {
    "a": "apple",
    "b": "banana",
    "c": "cherry"
}
hello_world = "hello world"
string = ""

if __name__ == "__main__":
    # for loops allow us to iterate over 
    # arrays (lists) or objects (dicts)
    for number in numbers:
        print(f'{number}')

    for key in dictionary:
        print(f'{dictionary[key]} is stored in {key}')

    # while loops allow us to iterate 
    # as long as a condition is true
    while len(string) < 10:
        string = string + "a"
        print(f'{string}')

    # if statements help us run certain operations
    # under certain conditions
    for i in hello_world:
        if i == "l":
            print(i)
        else:
            print('not l')

    # try-except blocks attempt to run code
    # that might fail without breaking the entire script
    try:
        f = open('folder_of_files/names.txt', 'r')
        text = f.read()
        list_of_rows_in_text = text.split('\n')
        for i in list_of_rows_in_text:
            print(f'The name, {i}, appeared in the file')
    except:
        print('There was a problem opening the file')
    
    
    
