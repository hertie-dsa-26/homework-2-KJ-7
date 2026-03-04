def evaluate_rpn(expression: str) -> float:
    """Evaluate a Reverse Polish Notation expression using a stack.

    Tokens must be separated by spaces. Supported operators: + - * /

    Examples:
        evaluate_rpn("3 4 +")               -> 7.0
        evaluate_rpn("5 1 2 + 4 * + 3 -")  -> 14.0
    """
    stack = []
    operators = {'+', '-', '*', '/'}

    for token in expression.split():
        if token in operators:
            if len(stack) < 2:
                raise ValueError(f"Not enough operands for operator '{token}'")
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                if b == 0:
                    raise ValueError("Division by zero")
                stack.append(a / b)
        else:
            try:
                stack.append(float(token))
            except ValueError:
                raise ValueError(f"'{token}' is not a valid number or operator")

    if len(stack) != 1:
        raise ValueError(f"Invalid expression: {len(stack)} value(s) left on the stack")
    return stack[0]
