# #Basic implementation
# #calculator addition following TDD
# def add_numbers(a: int, b: int) -> int:
#     return a + b

# #calculator multiplication following TDD
# def multiply_numbers(a: int, b: int) -> int:
#     return a * b

# #calculator division following TDD
# def divide_numbers(a: int, b: int) -> int:
#     return a / b

#Robust implementation
# from typing import Union
# from decimal import Decimal

# class CalculatorError(Exception):
# #Custom exception for calculator errors
#     pass

# def validate_numbers(a: Union[int, float], b: Union[int, float]) -> None:
#     if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
#         raise TypeError("Inputs must be numbers")

# def add_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
#     validate_numbers(a, b)
#     return a + b

# def multiply_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
#     validate_numbers(a, b)
#     return a * b

# def divide_numbers(a: Union[int, float], b: Union[int, float]) -> float:
#     validate_numbers(a, b)
#     if b == 0:
#         raise ZeroDivisionError("Cannot divide by zero")
#     return a / b

# def subtract_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
#     validate_numbers(a, b)
#     return a - b

import logging
from typing import Union
from functools import wraps

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('calculator.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Custom exception
class CalculatorError(Exception):
    #Custom exception for calculator errors
    pass

# Decorator for error handling and logging
def error_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            logger.info(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
            result = func(*args, **kwargs)
            logger.info(f"Result: {result}")
            return result
        except TypeError as e:
            logger.error(f"TypeError in {func.__name__}: {str(e)}")
            raise CalculatorError(f"Invalid input types: {str(e)}")
        except ZeroDivisionError as e:
            logger.error(f"ZeroDivisionError in {func.__name__}")
            raise CalculatorError("Division by zero is not allowed")
        except Exception as e:
            logger.error(f"Unexpected error in {func.__name__}: {str(e)}")
            raise CalculatorError(f"Unexpected error: {str(e)}")
    return wrapper

@error_handler
def add_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a + b

@error_handler
def subtract_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a - b

@error_handler
def multiply_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a * b

@error_handler
def divide_numbers(a: Union[int, float], b: Union[int, float]) -> float:
    if b == 0:
        raise ZeroDivisionError("Division by zero")
    return a / b