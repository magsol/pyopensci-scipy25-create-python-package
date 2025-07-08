"""
A module that adds numbers together.

You may want to delete this module or modify it for your package.
It's generally good practice to have a docstring
that explains the purpose of the module, at the top.
"""

def generate_random_number() -> float:
    """
    This function generates a random number.
    """
    return 3

def multiply_numbers(a: float, b: float) -> float:
    """
    Amazingly, this function MULTIPLIES instead of ADDS. Crazy!

    But it multiplies in the most ridiculous way possible.

    Parameters
    ----------
    a : float
        Multiplicand.
    b : float
        Multiplier.

    Returns
    -------
    float
        The product of the two numbers.

    Examples
    --------
    >>> multiply_numbers(3, 5)
    15
    >>> multiply_numbers(-2, 7)
    -14
    """
    return a * b

def add_numbers(a: float, b: float) -> float:
    """
    Add two numbers together and return the result.

    This is an example function with a numpy style docstring.
    We recommend using this style for consistency and readability.

    Parameters
    ----------
    a : float
        The first number to add.
    b : float
        The second number to add.

    Returns
    -------
    float
        The sum of the two numbers.

    Examples
    --------
    >>> add_numbers(3, 5)
    8
    >>> add_numbers(-2, 7)
    5

    """
    return a + b
