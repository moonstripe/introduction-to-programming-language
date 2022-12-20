---
marp: true
---
# Introduction to Python
---
# Basic Types

basic types are the building blocks of meaningful code

our communication relies on us being consistent about them.

``` python
# strings or str
hello = "hello"
world = "world"

# integers or int
one = 1
two = 2

# floats
almost_zero = 0.01
almost_one = 0.99

# booleans
factual = True
fictitious = False
```

---
This should work:
``` python
# concatenate strings together
print(f'Concatinating strings: {hello + " " + world}')

# adding numbers together:
print(f'Adding integers: {one + two}')

# adding floats together:
print(f'Adding floats: {almost_zero + almost_one}')

# adding a float to an integer
print(f'Adding a float to an integer: {one + almost_one}')
```

---
However this will not:
``` python
print(f'This printline will not appear due to an error: {hello + one}')
```
<br/>

Instead of what we wanted, we were presented with:
```
Traceback (most recent call last):
  File ".../a_basic_types.py", line 60, in <module>
    print(f'This printline will not appear due to an error: {hello + one}')
                                                             ~~~~~~^~~~~
TypeError: can only concatenate str (not "int") to str
```
---
# Collections
basic collections are powerful ways to store basic types...

```python
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
```
---
...so we can use them later
```python
# we can "destructure" tuples
lat, long = another_coordinate

print(f'another_coordinate, Latitude: {lat}, Longitude: {long}')

# get element at index 4
print(f'In list of programs, the program stored at index 4 is {programs[4]}')

# get index of "IPD" from list
print(f'In list of programs, "IPD" is stored at index {programs.index("IPD")}')

# get value from key "123 Main St":
print(f'The inhabitants of "123 Main St": {building_reference["123 Main St"]}')
```
---
we might add to them and subtract from them, too
```python
# adding PYTH to list of programs
programs.append("PYTH")
print(f'Program list: {programs}')

# removing the the item at index 8
programs.pop(8)
print(f'Program list: {programs}')

# adding a new family to building_reference
building_reference["127 Main St"] = ["本名和子", "本名智", "本名武"]
print(f'Building reference: {building_reference}')

# removing a family from building_reference
building_reference.pop("123 Main St)
print(f'Building reference: {building_reference}')


```
---
`NOTE`: you cannot add elements to tuples, but you can add to lists and dicts.

```python
# this line fails:
# another_coordinate.append(99.9999)
```
<br/>
<br/>
<br/>

but I use collections the most when I'm writing loops!

---
# Control Flow

control flow is how we direct how programs operate under certain circumstances

we can break down the concept of control flow into loops and conditionals

```python
numbers = [1, 2, 3, 4, 5]
dictionary = {
    "a": "apple",
    "b": "banana",
    "c": "clementine"
}
string = ""
```

---
## Loops
loops run a set of instructions continuously until they stop
- for loops:
  - run as many times as there are elements in a tuple, list, or dict
  - "for every item in this list, run program"
- while loops
  - run for as long as a condition is met
  - "while something is true, run program"

---
for loops allow us to iterate over tuples, arrays (`list`) or objects (`dict`)
```python
# iterating over a list 
for number in numbers:
    print(f'{number} x 5 is {number * 5}')

# iterating over an dict
for key in dictionary:
    print(f'{dictionary[key]} is stored in {key}')
```
pro-tip: with a `list`, you can also pull index values by enumerating the `list`
```python
for index, number in enumerate(numbers):
    print(f'index: {index}, number: {number}')
```
---
while loops allow us to iterate as long as a condition is true
```python
while len(string) < 10:
    string = string + "a"
    print(f'{string}')
```
`NOTE`: unless you have a specific reason to use them, while loops can be more dangerous than they are useful, especially when dealing with any kind of network communication.

---
## Conditionals

conditionals determine whether certain code should be run.
- if statements:
  - determine whether code runs according to specified conditions
  - "if something is true, run program(, or else run another program)"
- try, except statements:
  - will run until it hits an obstacle, and then allows predefined error behavior.
  - "try running a program, and then if something goes wrong, run another program"
  - *particularly useful in working with networked information*
---
if statements allow us to run certain operations under certain conditions
```python
for number in numbers:
    if number % 2 == 0:
        print(f'{number} is divisible by 2')
    else:
        print(f'{number} is not divisible by 2')
```
---
try-except statements attempt to run code that might fail without breaking the entire script
```python
try:
    f = open('folder_of_files/names.txt', 'r')
    text = f.read()
    list_of_rows_in_text = text.split('\n')
    for i in list_of_rows_in_text:
        print(f'The name, {i}, appeared in the file')
except:
    print('There was a problem opening the file')
```
---