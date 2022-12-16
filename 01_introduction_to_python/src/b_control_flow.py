# Nothing to import

# control flow is how we dictate how
# programs operate in certain circumstance

# for loops allow us to iterate over arrays (lists) or objects (dicts)
numbers = [1, 2, 3, 4, 5]
s = {
    ""
}

for number in numbers:
    print(f'{number}')

# while loops allow us to iterate 
# as long as a condition is true
string = ""

while len(string) < 10:
    string = string + "a"
    print(f'{string}')

# if statements help us run certain operations
# under certain conditions

hello_world = "hello world"

for i in hello_world:
    if i == "l":
        print(i)


if __name__ == "__main__":
    pass