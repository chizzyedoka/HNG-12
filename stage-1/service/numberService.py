import math
from typing import List

import requests

def is_valid_number(value) -> bool:
    """
    Check if a string represents a valid integer, including negative numbers.
    Returns True for valid integers (including negative), False otherwise.
    """
    if not value:
        return False
    
    # Handle the case of just a minus sign
    if value == '-' or '-' in value:
        return False
        
    # Check if it's a valid integer string
    try:
        int(value)
        return True
    except ValueError:
        return False
    
def is_numeric(value):
    """
    Check if a value can be converted to a numeric type (int or float).
    
    Args:
        value: Any type of input
        
    Returns:
        bool: True if the value can be converted to a number, False otherwise
        
    Examples:
        >>> is_numeric("123")     # True
        >>> is_numeric("-123.45") # True
        >>> is_numeric("abc")     # False
        >>> is_numeric(None)      # False
        >>> is_numeric("")        # False
    """
    if value is None:
        return False
        
    # Convert to string if not already
    if not isinstance(value, str):
        value = str(value)
        
    # Remove whitespace
    value = value.strip()
    
    # Handle empty string
    if not value:
        return False
        
    # Handle negative numbers and decimals
    value = value.replace('-', '', 1)  # Remove first minus sign if exists
    value = value.replace('.', '', 1)  # Remove first decimal point if exists
    
    # Check if remaining string contains only digits
    return value.isdigit()

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