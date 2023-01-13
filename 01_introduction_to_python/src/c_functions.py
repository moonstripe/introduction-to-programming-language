from typing import Callable
from b_control_flow import numbers

def add_one(number):
    new_number = number + 1
    return new_number

age = 26

example = add_one(age)

print(f'This is the value of new_number: {example}')

def typed_add_one(number: int) -> int:
    new_number = number + 1
    return new_number

age_plus_one = typed_add_one(age)

print(f'The new age is now: {age_plus_one}')

def apply_math_to_list(math_function: Callable, list_of_numbers: list[int]) -> list[int]:
    return_arr: list[int] = []

    for number in list_of_numbers:
        math_applied = math_function(number)
        return_arr.append(math_applied)
    
    return return_arr

new_numbers = apply_math_to_list(typed_add_one, numbers)

print(f'Applying the function to all numbers, the new list is : {new_numbers}')

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
        'data': 'cherry'
    }
}

def recursive_function(linked_item: dict, data_array: list):
    
    new_item = linked_item['data']

    data_array.append(new_item)

    if 'next_page' in list(linked_item.keys()):
        next_page = linked_item['next_page']
        recursive_function(linked_info[next_page], data_array)

    return data_array

print(f'Result of Pull: {recursive_function(linked_info["0"], [])}')