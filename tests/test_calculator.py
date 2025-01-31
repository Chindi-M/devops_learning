# #Basic implementation
# #test calculator following TDD
# def test_add_numbers():
#     #Import the function add_numbers from calculator.py
#     from calculator import add_numbers
#     #Test basic addition
#     assert add_numbers(2,3) == 5
#     #Test negative numbers
#     assert add_numbers(-1, 1) == 0
#     #Test zero
#     assert add_numbers(0, 0) == 0

# def test_multiply_numbers():
#     #Import the function multiply_numbers from calculator.py
#     from calculator import multiply_numbers
#     #Test basic multiplication
#     assert multiply_numbers(2, 3) == 6
#     #Test negative numbers
#     assert multiply_numbers(-2, 3) == -6
#     #Test zero
#     assert multiply_numbers(0, 5) == 0

# def test_divide_numbers():
#     from calculator import divide_numbers
#     assert divide_numbers(6, 2) == 3
#     assert divide_numbers(-6, 2) == -3
#     assert divide_numbers(5, 2) == 2.5

#     try:
#         divide_numbers(4, 0)
#         assert False, "Should have raised ZeroDivisionError"
#     except ZeroDivisionError:
#         assert True

#Robust implementation
# import pytest
# from calculator import (
#     add_numbers,
#     multiply_numbers,
#     divide_numbers,
#     subtract_numbers,
#     CalculatorError
# )

# # Fixtures
# @pytest.fixture
# def sample_numbers():
#     return {
#         "integers": (10, 5),
#         "floats": (10.5, 2.5),
#         "negatives": (-10, -5),
#         "zero": (0, 0)
#     }

# # Parameterized Tests
# @pytest.mark.parametrize("a, b, expected", [
#     (10, 5, 15),
#     (-1, 1, 0),
#     (0, 0, 0),
#     (10.5, 2.5, 13.0)
# ])
# def test_add_numbers_parametrized(a, b, expected):
#     assert add_numbers(a, b) == expected

# @pytest.mark.parametrize("a, b, expected", [
#     (10, 5, 50),
#     (-2, 3, -6),
#     (0, 5, 0),
#     (2.5, 2, 5.0)
# ])
# def test_multiply_numbers_parametrized(a, b, expected):
#     assert multiply_numbers(a, b) == expected

# # Using Fixtures
# def test_operations_with_fixture(sample_numbers):
#     integers = sample_numbers["integers"]
#     assert add_numbers(*integers) == 15
#     assert multiply_numbers(*integers) == 50
#     assert divide_numbers(*integers) == 2

# # Exception Testing
# def test_division_exceptions():
#     with pytest.raises(ZeroDivisionError):
#         divide_numbers(4, 0)

#     with pytest.raises(TypeError):
#         divide_numbers("4", 2)

# # Integration Tests
# @pytest.mark.integration
# def test_chained_operations():
#     # (10 + 5) * 2 / 5
#     result = divide_numbers(
#         multiply_numbers(
#             add_numbers(10, 5),
#             2
#         ),
#         5
#     )
#     assert result == 6

# # Critical Tests
# @pytest.mark.critical
# def test_critical_operations():
#     assert add_numbers(1000000, 1000000) == 2000000
#     assert divide_numbers(1, 3) == pytest.approx(0.3333333)

# # Mock Example (if we had external dependencies)
# from unittest.mock import Mock, patch

# @pytest.mark.mock
# def test_with_mock():
#     mock_dependency = Mock()
#     mock_dependency.get_value.return_value = 42
#     with patch('calculator.some_external_dependency', mock_dependency):
#         assert True  # Replace with actual test if we add dependencies

# test_calculator.py
import pytest
from calculator import *

# New comprehensive test suite
class TestCalculator:
    @pytest.mark.smoke
    def test_basic_operations(self):
        """Test all basic operations with simple numbers"""
        assert add_numbers(2, 2) == 4
        assert subtract_numbers(4, 2) == 2
        assert multiply_numbers(3, 3) == 9
        assert divide_numbers(8, 2) == 4

    @pytest.mark.edge_cases
    def test_edge_cases(self):
        """Test edge cases like zero, negative numbers"""
        assert add_numbers(0, 0) == 0
        assert multiply_numbers(0, 5) == 0
        assert subtract_numbers(-1, -1) == 0

        with pytest.raises(ZeroDivisionError):
            divide_numbers(5, 0)

    @pytest.mark.parametrize("operation,a,b,expected", [
        (add_numbers, 5, 5, 10),
        (subtract_numbers, 10, 5, 5),
        (multiply_numbers, 3, 4, 12),
        (divide_numbers, 15, 3, 5)
    ])
    def test_parametrized_operations(self, operation, a, b, expected):
        """Test multiple operations with different values"""
        assert operation(a, b) == expected

    def test_error_handling(self):
        """Test error handling and logging"""
        with pytest.raises(CalculatorError):
            divide_numbers(5, 0)

        with pytest.raises(CalculatorError):
            add_numbers("5", 5)

        with pytest.raises(CalculatorError):
            multiply_numbers(None, 5)