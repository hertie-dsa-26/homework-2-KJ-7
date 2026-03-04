def perform_calculation(value1, value2, operation: str, integer_mode: bool = False):
    """Perform a mathematical operation on two values."""
    if operation == 'add':
        return value1 + value2
    elif operation == 'subtract':
        return value1 - value2
    elif operation == 'divide':
        # Use floor division in integer mode so the result stays a whole number
        return value1 // value2 if integer_mode else value1 / value2
    else:
        return value1 * value2


def convert_input(value1: str, value2: str, numtype: str):
    """Convert two strings to int or float depending on numtype."""
    if numtype == 'int':
        return int(value1), int(value2)
    return float(value1), float(value2)

