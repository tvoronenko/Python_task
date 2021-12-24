from collections import deque


def postfix(prefix):
    stack = deque()

    prefix = ''.join((reversed(prefix)))  # Reversing the expression
    for symbol in prefix:

        if symbol != '+' and symbol != '-' and symbol != '*' and symbol != '/':
            stack.append(symbol)  # Push if an operand

        else:
            # If an operator, then pop two operands from stack
            operand1 = stack.pop()
            operand2 = stack.pop()
            # Concatenate operands and operator and again push it in stack
            stack.append(operand1 + operand2 + symbol)

    return (stack.pop())  # Poping the result


print(postfix('*-A/BC+/AKL')) #ABC/-AK/L+*
