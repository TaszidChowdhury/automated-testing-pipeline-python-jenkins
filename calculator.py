"""
Simple Calculator Module
Provides basic arithmetic operations and some advanced mathematical functions.
"""

import math
from typing import Union, List


class Calculator:
    """A simple calculator class with basic and advanced mathematical operations."""
    
    def __init__(self):
        self.history = []
    
    def add(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Add two numbers."""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Subtract b from a."""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Multiply two numbers."""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Divide a by b."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def power(self, base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
        """Raise base to the power of exponent."""
        result = base ** exponent
        self.history.append(f"{base} ^ {exponent} = {result}")
        return result
    
    def square_root(self, number: Union[int, float]) -> float:
        """Calculate the square root of a number."""
        if number < 0:
            raise ValueError("Cannot calculate square root of negative number")
        result = math.sqrt(number)
        self.history.append(f"√{number} = {result}")
        return result
    
    def factorial(self, n: int) -> int:
        """Calculate the factorial of a non-negative integer."""
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        self.history.append(f"{n}! = {result}")
        return result
    
    def average(self, numbers: List[Union[int, float]]) -> float:
        """Calculate the average of a list of numbers."""
        if not numbers:
            raise ValueError("Cannot calculate average of empty list")
        result = sum(numbers) / len(numbers)
        self.history.append(f"Average of {numbers} = {result}")
        return result
    
    def clear_history(self):
        """Clear the calculation history."""
        self.history.clear()
    
    def get_history(self) -> List[str]:
        """Get the calculation history."""
        return self.history.copy()


# Standalone functions for convenience
def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Add two numbers."""
    return a + b


def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Subtract b from a."""
    return a - b


def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Multiply two numbers."""
    return a * b


def divide(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b 