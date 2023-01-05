---
marp: true
---
# Introduction to Python
---
# Basic Types

basic types are the primary building blocks of meaningful code, like words

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
this should work:
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
however this will not:
``` python
print(f'This printline will not appear due to an error: {hello + one}')
```
<br/>

instead of what we wanted, we were presented with:
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

but collections are the most useful when paired with loops ![width:500px bg right](https://i.kym-cdn.com/photos/images/newsfeed/001/393/656/da7.jpg)

---
# Control Flow

control flow dictates how programs operate under certain circumstances

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
  - **particularly useful in working with networked information**
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
    f.close()
except:
    print('There was a problem opening the file')
```
---

as we become more involved with communicating in code, we also need to better organize our own thoughts

an important first step to clearer communication is by knowing how to **define functions**

---
# Functions

a function is a useful tool for organizing repeatable code
- think about it as the predicate (verb) we need to use in order to make sentences out of variables (words)

functions take *parameters*, and then return a *value*

---
we use the `def` keyword to initialize a function, and in the parentheses, we add our parameters

the indented line returns a value

```python
def add_one(number):
    new_number = number + 1
    return new_number
```

now this function can be used wherever
```python
age = 25

print(f'The current age is: {age}')

age_plus_one = add_one(age)

print(f'The new age is now: {age_plus_one}')
```
---
scope defines where certain variables are usable
```python
number = 66

def add_one(number):
    new_number = number + 1
    return new_number

example = add_one(number)

print(f'This is the value of new_number: {new_number}')
print(f'This is the value of example: {example}')
```
here, the value `new_number` is only "in scope" inside the definition of the `add_one` function

after, the variable name is freed, allowing us to define it as something else

---
in more recent versions of Python, we can be explicit about what types parameters are and what type the return value will be

```python
    def typed_add_one(number: int) -> int:
        new_number = number + 1
        return new_number
    
    age_plus_one = typed_add_one(age)

    print(f'The new age is now: {age_plus_one}')
```

this helps us remember what each function does, and what we can expect out of them.

---

functions can take other functions, too
```python
from typing import Callable

def apply_math_to_list(math_function: Callable, list_of_numbers: list[int]) -> list[int]:

    return_arr: list[int] = []

    for number in list_of_numbers:
        math_applied = math_function(number)
        return_arr.append(math_applied)

    return return_arr
```
---

when we pass a first function to a second function, we don't have to call it in the second function's parameter.
```python
numbers = [1, 2, 3, 4, 5]

new_numbers = apply_math_to_list(typed_add_one, numbers)

print(f'Applying the function to all numbers, the new list is:{new_numbers}')
```
---

recursion is when a function calls itself until a condition is met.

this is especially useful when collecting information from a list of linked elements.

```python
linked_info = {
    '0': {
        'data': 'apple',
        'next_page': '1'
    },
    '1': {
        'data': 'banana',
        'next_page': '2'
    },
    '2': {
        'data': 'cherry',
    }
}
```
---
```python
def recursive_function(linked_item: dict, data_array: list):

    new_item = linked_item['data']

    data_array.append(new_item)

    if 'next_page' in list(linked_item.keys()):
        next_page = linked_item['next_page']
        recursive_function(linked_info[next_page], data_array)

    return data_array

print(f'Result: {recursive_function(linked_info["0"], [])}')
```

now that you can deftly use sentences to talk to computers, it's time to learn how to form more complete thoughts, with classes

---
# Classes

if types and collections are words, functions are verbs with which we can form sentences, classes are paragraphs that allow us to make a point

they are a conceptual combination of data and functions that allow us to organize our code even more effectively
- it's up to us to make them as specific or as broad as we want them

steps to using classes:
1. we define what our class looks like, and what kind of behaviors it will have
2. we "instantiate" it by assigning it to a variable

---
we use the `class` keyword to blueprint a new class.

```python
class Building:
```

next, we define initialization behavior with the `__init__` boilerplate method, passing in `self`, as well as all the information we need for our `Building`
```python
    def __init__(self, address: str, max_occupancy: int):
        self.address = address
        self.max_occupancy = max_occupancy

        self.unit_map: dict[str, None | str] = {}

        for unit in range(self.max_occupancy):
            self.unit_map[str(unit)] = None
```
here, we also include some code to create more data, the `unit_map`, using data we pulled into our `Building` definition.

`NOTE`: make sure your lines are properly indented

---

by adding our own custom methods, we can extend our `Building` to make transformations to itself.

```python
    def fill_vacancy(self, name: str) -> str:
        for unit in self.unit_map:
            if self.unit_map[unit] is None:
                self.unit_map[unit] = name

                print(f'Welcome to unit {unit}, {name}!')
                return unit
        
        raise Exception(f"No units found for {name}...")
```

the `raise` keyword is used for custom error handling, since it's possible to call `fill_vacancies` when the `Building` is full

---

we instantiate our `Building` class by assigning it to a variable
```python
# make an instance of a Building at 460 Pierce St. with 8 units in it.

new_dorm = Building('460 Pierce St', 8)


# we can access the information that we put into it, 
# and the other data that we created in initializing our Building

print(f'new_dorm address: {new_dorm.address}')

print(f'new_dorm maximum occupancy: {new_dorm.max_occupancy}')

print(f'new_dorm unit map: {new_dorm.unit_map}')
```
---

let's populate our `Building` by housing people

```python
students = ['kojin', 'steve', 'cathy', 'nicole', 'pablo', 'artem', 'cyril', 'cassandra', 'paul']

for student in students:
    new_dorm.fill_vacancy(student)
    print(f'Dorm Unit Map: {new_dorm.unit_map}')
```

if we check the response, it looks as though the building successfully housed 8 of 9 students, and returned a custom error message saying what happened with the last one

```
...
Dorm Unit Map: {'0': 'kojin', '1': 'steve', ..., '7': 'cassandra'}
Traceback (most recent call last):
  File ".../src/d_classes.py", line 37, in <module>
    new_dorm.fill_vacancy(student)
  File ".../src/d_classes.py", line 20, in fill_vacancy
    raise Exception(f"No units found for {name}")
Exception: No units found for paul
```

---

# Libraries

you are never expected to recreate the wheel every time you write a program
- there are built-in modules that you can access
- you may have already solved a relevant problem earlier
- smart people have made wonderful packages that you can use for free

---

using the `import` keyword, we can access the built-in libraries, like `random` or `datetime`.

```python
import random
import datetime as dt

# random: randomization functions
print(f'Random float between 0 and 1: {random.random()}')

candies = ['red m&m', 'orange m&m', 'red m&m', 'green m&m', 'blue m&m']

print(f'Random candy choice: {random.choice(candies)}')

# datetime: functions related to telling the time
now = dt.datetime.today()

print(f'Right now: {now}')
```

`NOTE`: for readability, import statements should always be at the top of a script.

---
we can `import` things from our existing files.

by using the `from` keyword before `import` we can specify which resources we need from a library.

```python
from d_classes import Building

another_dorm = Building('411 Pacific St', 5)

another_dorm.fill_vacancy('carl')

print(f'Occupants of {another_dorm.address}: {another_dorm.unit_map}')
```

---

`pip` is your portal into other developers' work

to check if we are in the correct environment, in your **Terminal**, you should see:

```zsh
(env) your_username@your_machine file_path % 
```
then, to install a package into the environment, 
```zsh
(env) your_username@your_machine file_path % pip install scamp
```
---
now we can `import` scamp into our code

```python
# SCAMP or Suite for Computer Assisted Music Production 
# is a library that allows us to write music

from scamp import *

middle_c_midi = 60

c_scale = []

s = Session()

clarinet = s.new_part('clarinet')

clarinet.play_note(middle_c_midi, 1, 1)
```
let's write a function that generates a scale which we can play

---
first, we need some fundamental information, called constants.

```python
# we typically assign constants to all-caps variables
MODE_DICT = {
    'minor': ['W', 'H', 'W', 'W', 'H', 'W', 'W'],
    'major': ['W', 'W', 'H', 'W', 'W', 'W', 'H']
}

MIDDLE_NOTES = {
    'a': 57,
    'a_sharp': 58,
    'b': 59,
    'c': 60,
    'c_sharp': 61,
    'd': 62,
    'd_sharp': 63,
    'e': 64,
    'f': 65,
    'f_sharp': 66,
    'g': 67,
    'g_sharp': 68
}
```
---
now we can write a function that takes a key and a mode (major or minor) and writes a scale
```python
# we can use multi-line strings to add notes about our function
def generate_scale(note: str = "c", mode: str = 'major') -> list:
    """
        This function generates a scale based on the note and mode
    """
    scale = []

    stepper = MIDDLE_NOTES[note]

    for step in SCALE_DICT[mode]:
        if step == "W":
            scale.append(stepper)
            stepper = stepper + 2
        else:
            scale.append(stepper)
            stepper = stepper + 1

    return scale

```

---
let's test our code by playing the C Major scale

```python
s = Session()

piano = s.new_part('piano')

c_major = generate_scale('c', 'major')

for note in c_major:
    piano.play_note(note, 1, 1)
```
music to my ears!

---
# Exercise

to maximize productivity, many people listen to lyric-less music while they work

but finding songs to play that are new and exciting can be time consuming, ultimately defeating the purpose of being productive in the first place

using `scamp`, make a productivity tool that helps you study with music that is randomly generated.

extra credit: use the concept of chord progression in music theory to make even more compelling music

---
## Resources

learning how to use software you haven't written is the most crucial skill you can learn as a programmer

reading documentation, and even understanding source code can help you use software without risk of bugs or security flaws

[SCAMP documentation](http://scamp.marcevanstein.com/scamp.html)

--- 

