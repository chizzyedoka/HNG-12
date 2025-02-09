import math
from typing import List

import requests


def is_armstrong(num: int) -> bool:
    # Convert number to string to count digits
    num_str = str(num)
    power = len(num_str)
    # Calculate sum of each digit raised to power of number of digits
    total = sum(int(digit) ** power for digit in num_str)
    return total == num

def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def is_perfect(num: int) -> bool:
    if num <= 1:
        return False
    # Find sum of proper divisors
    divisor_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisor_sum == num

def get_digit_sum(num: int) -> int:
    return sum(int(digit) for digit in str(num))

def get_number_properties(num: int) -> List[str]:
    properties = []
    
    # Check if number is Armstrong
    if is_armstrong(num):
        properties.append("armstrong")
    
    # Check parity
    if num % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")
    
    return properties

def get_fun_fact(num: int) -> str:
    try:
        response = requests.get(f"http://numbersapi.com/{num}/math")
        if response.status_code == 200:
            return response.text
        else:
            return f"{num} is an interesting number with various mathematical properties."
    except:
        return f"{num} is an interesting number with various mathematical properties."