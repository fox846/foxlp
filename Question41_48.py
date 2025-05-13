import re

# Define precedence and associativity
precedence = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}
right_associative = {'^'}

# Function to convert infix to postfix using Shunting Yard
def infix_to_postfix(expr):
    tokens = re.findall(r'[a-zA-Z_]\w*|\d+|[+*/^()-]', expr)
    output = []
    stack = []

    for token in tokens:
        if re.match(r'[a-zA-Z_]\w*|\d+', token):  # Variable or number
            output.append(token)
        elif token in precedence:
            while (stack and stack[-1] != '(' and
                   (precedence[stack[-1]] > precedence[token] or
                   (precedence[stack[-1]] == precedence[token] and token not in right_associative))):
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
    while stack:
        output.append(stack.pop())
    return output

# Generate TAC from postfix
def generate_TAC(postfix):
    stack = []
    temp_count = 1
    code = []
    
    for token in postfix:
        if token not in precedence:
            stack.append(token)
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            temp = f't{temp_count}'
            code.append(f'{temp} = {op1} {token} {op2}')
            stack.append(temp)
            temp_count += 1
    return code, stack.pop()

# Wrapper to process full expression with assignment
def process_expression(expression):
    if '=' in expression:
        lhs, rhs = [part.strip() for part in expression.split('=')]
    else:
        lhs, rhs = None, expression.strip()
    postfix = infix_to_postfix(rhs)
    tac, final_result = generate_TAC(postfix)
    for line in tac:
        print(line)
    if lhs:
        print(f'{lhs} = {final_result}')

# Run for all given expressions
expressions = [
    "w = u*u - u*v + v*v",
    "y = x*x + w - v / r + r",
    "w = u*u - u*v + v*v",
    "t = o*a - o*b + o*c",
    "t = j / k - y / u - i",
    "a = m * n - o - p / q",
    "a = f ^ r - u * f * t - p",
    "a = (b*b + c*c) * (p - q - r)"
]

print("### Three Address Code Generator ###\n")
for idx, expr in enumerate(expressions, 1):
    print(f"({idx + 41}) Input: {expr}")
    process_expression(expr)
    print("+" * 40)
