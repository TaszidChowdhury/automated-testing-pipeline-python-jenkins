"""
Test cases for the Calculator module using pytest.
"""

import pytest
from calculator import Calculator, add, subtract, multiply, divide


class TestCalculator:
    """Test class for Calculator methods."""
    
    def setup_method(self):
        """Set up a fresh calculator instance before each test."""
        self.calc = Calculator()
    
    def test_add_integers(self):
        """Test addition with integers."""
        assert self.calc.add(5, 3) == 8
        assert self.calc.add(-5, 3) == -2
        assert self.calc.add(0, 0) == 0
    
    def test_add_floats(self):
        """Test addition with floats."""
        assert self.calc.add(5.5, 3.2) == 8.7
        assert self.calc.add(-5.5, 3.2) == -2.3
        assert self.calc.add(0.0, 0.0) == 0.0
    
    def test_subtract_integers(self):
        """Test subtraction with integers."""
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(-5, 3) == -8
        assert self.calc.subtract(0, 0) == 0
    
    def test_subtract_floats(self):
        """Test subtraction with floats."""
        assert self.calc.subtract(5.5, 3.2) == 2.3
        assert self.calc.subtract(-5.5, 3.2) == -8.7
        assert self.calc.subtract(0.0, 0.0) == 0.0
    
    def test_multiply_integers(self):
        """Test multiplication with integers."""
        assert self.calc.multiply(5, 3) == 15
        assert self.calc.multiply(-5, 3) == -15
        assert self.calc.multiply(0, 5) == 0
    
    def test_multiply_floats(self):
        """Test multiplication with floats."""
        assert self.calc.multiply(5.5, 3.2) == 17.6
        assert self.calc.multiply(-5.5, 3.2) == -17.6
        assert self.calc.multiply(0.0, 5.0) == 0.0
    
    def test_divide_integers(self):
        """Test division with integers."""
        assert self.calc.divide(6, 2) == 3.0
        assert self.calc.divide(-6, 2) == -3.0
        assert self.calc.divide(0, 5) == 0.0
    
    def test_divide_floats(self):
        """Test division with floats."""
        assert self.calc.divide(6.0, 2.0) == 3.0
        assert self.calc.divide(-6.0, 2.0) == -3.0
        assert self.calc.divide(0.0, 5.0) == 0.0
    
    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(5, 0)
    
    def test_power_integers(self):
        """Test power operation with integers."""
        assert self.calc.power(2, 3) == 8
        assert self.calc.power(2, 0) == 1
        assert self.calc.power(0, 5) == 0
    
    def test_power_floats(self):
        """Test power operation with floats."""
        assert self.calc.power(2.0, 3.0) == 8.0
        assert self.calc.power(2.5, 2.0) == 6.25
        assert self.calc.power(0.0, 5.0) == 0.0
    
    def test_square_root_positive(self):
        """Test square root with positive numbers."""
        assert self.calc.square_root(4) == 2.0
        assert self.calc.square_root(9) == 3.0
        assert self.calc.square_root(0) == 0.0
    
    def test_square_root_negative(self):
        """Test square root with negative numbers raises ValueError."""
        with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
            self.calc.square_root(-4)
    
    def test_factorial_positive(self):
        """Test factorial with positive integers."""
        assert self.calc.factorial(0) == 1
        assert self.calc.factorial(1) == 1
        assert self.calc.factorial(5) == 120
        assert self.calc.factorial(10) == 3628800
    
    def test_factorial_negative(self):
        """Test factorial with negative numbers raises ValueError."""
        with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
            self.calc.factorial(-5)
    
    def test_average_positive_numbers(self):
        """Test average calculation with positive numbers."""
        assert self.calc.average([1, 2, 3, 4, 5]) == 3.0
        assert self.calc.average([1.5, 2.5, 3.5]) == 2.5
        assert self.calc.average([10]) == 10.0
    
    def test_average_empty_list(self):
        """Test average calculation with empty list raises ValueError."""
        with pytest.raises(ValueError, match="Cannot calculate average of empty list"):
            self.calc.average([])
    
    def test_history_functionality(self):
        """Test that calculations are recorded in history."""
        self.calc.add(5, 3)
        self.calc.multiply(2, 4)
        self.calc.divide(10, 2)
        
        history = self.calc.get_history()
        assert len(history) == 3
        assert "5 + 3 = 8" in history
        assert "2 * 4 = 8" in history
        assert "10 / 2 = 5.0" in history
    
    def test_clear_history(self):
        """Test clearing calculation history."""
        self.calc.add(5, 3)
        self.calc.multiply(2, 4)
        
        assert len(self.calc.get_history()) == 2
        
        self.calc.clear_history()
        assert len(self.calc.get_history()) == 0


class TestStandaloneFunctions:
    """Test class for standalone calculator functions."""
    
    def test_add_function(self):
        """Test standalone add function."""
        assert add(5, 3) == 8
        assert add(-5, 3) == -2
        assert add(0, 0) == 0
        assert add(5.5, 3.2) == 8.7
    
    def test_subtract_function(self):
        """Test standalone subtract function."""
        assert subtract(5, 3) == 2
        assert subtract(-5, 3) == -8
        assert subtract(0, 0) == 0
        assert subtract(5.5, 3.2) == 2.3
    
    def test_multiply_function(self):
        """Test standalone multiply function."""
        assert multiply(5, 3) == 15
        assert multiply(-5, 3) == -15
        assert multiply(0, 5) == 0
        assert multiply(5.5, 3.2) == 17.6
    
    def test_divide_function(self):
        """Test standalone divide function."""
        assert divide(6, 2) == 3.0
        assert divide(-6, 2) == -3.0
        assert divide(0, 5) == 0.0
        assert divide(6.0, 2.0) == 3.0
    
    def test_divide_function_by_zero(self):
        """Test standalone divide function with zero divisor."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)


class TestCalculatorEdgeCases:
    """Test class for edge cases and boundary conditions."""
    
    def setup_method(self):
        """Set up a fresh calculator instance before each test."""
        self.calc = Calculator()
    
    def test_large_numbers(self):
        """Test operations with large numbers."""
        large_num = 999999999
        assert self.calc.add(large_num, 1) == 1000000000
        assert self.calc.multiply(large_num, 0) == 0
    
    def test_floating_point_precision(self):
        """Test floating point precision."""
        result = self.calc.add(0.1, 0.2)
        assert abs(result - 0.3) < 1e-10
    
    def test_mixed_types(self):
        """Test operations with mixed integer and float types."""
        assert self.calc.add(5, 3.5) == 8.5
        assert self.calc.multiply(2, 3.5) == 7.0
        assert self.calc.divide(7, 2) == 3.5
    
    def test_zero_operations(self):
        """Test various operations with zero."""
        assert self.calc.add(0, 0) == 0
        assert self.calc.subtract(0, 0) == 0
        assert self.calc.multiply(0, 5) == 0
        assert self.calc.divide(0, 5) == 0.0
        assert self.calc.power(0, 5) == 0
        assert self.calc.square_root(0) == 0.0
    
    def test_negative_operations(self):
        """Test operations with negative numbers."""
        assert self.calc.add(-5, -3) == -8
        assert self.calc.subtract(-5, -3) == -2
        assert self.calc.multiply(-5, -3) == 15
        assert self.calc.divide(-6, -2) == 3.0
        assert self.calc.power(-2, 3) == -8 