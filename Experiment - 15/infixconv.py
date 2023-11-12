class ExpressionConverter:
    def __init__(self):
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def infix_to_postfix(self, expression):
        result = []
        stack = []
        for token in expression:
            if token.isalnum():
                result.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    result.append(stack.pop())
                stack.pop()
            else:
                while stack and stack[-1] != '(' and self.precedence.get(token, 0) <= self.precedence.get(stack[-1], 0):
                    result.append(stack.pop())
                stack.append(token)
        while stack:
            result.append(stack.pop())
        return result

    def infix_to_prefix(self, expression):
        expression = expression[::-1]
        for i in range(len(expression)):
            if expression[i] == '(':
                expression[i] = ')'
            elif expression[i] == ')':
                expression[i] = '('
        return self.infix_to_postfix(expression)[::-1]

    def generate_three_address_code(self, postfix):
        stack = []
        count = 1
        for token in postfix:
            if token.isalnum():
                stack.append(token)
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                result = f't{count}'
                print(f'{result} = {op1} {token} {op2}')
                stack.append(result)
                count += 1

expression = "a+b*(c^d-e)^(f+g*h)-i"
converter = ExpressionConverter()
postfix = converter.infix_to_postfix(list(expression))
print("Postfix is:", ''.join(postfix))
prefix = converter.infix_to_prefix(list(expression))
print("Prefix is:", ''.join(prefix))
print("Three-address code:")
converter.generate_three_address_code(postfix)
