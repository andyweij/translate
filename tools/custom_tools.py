from langchain_core.tools import tool

@tool
def add(a: int, b: int) -> int:
    """Adds two integers.

    Args:
        a: First integer
        b: Second integer
    """
    return a + b

@tool
def multiply(a: int, b: int) -> int:
    """Multiplies two integers.

    Args:
        a: First integer
        b: Second integer
    """
    return a * b

@tool
def magic_function(input: int) -> int:
    """Applies a magic operation to an integer.
    
    Args:
        input: The input integer.
    """
    return input + 2
