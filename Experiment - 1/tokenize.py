import tokenize
import io
import keyword
import re

keywords = set(keyword.kwlist)
operators = {'+', '-', '*', '**', '/', '//', '%', '@', '<<', '>>', '&', '|', '^', '~', ':=', '<', '>', '<=', '>=', '==', '!='}
delimiters = {'=', '(', ')', '[', ']', '{', '}', ',', ':', '.', ';', '@', '=', '->', '+=', '-=', '*=', '/=', '//=', '%=', '@=', '&=', '|=', '^=', '>>=', '<<=', '**='}
identifiers = set()
numbers = set()


with open('input.py', 'r') as file:
    code = file.read()

tokens = tokenize.tokenize(io.BytesIO(code.encode('utf-8')).readline)

for toknum, tokval, _, _, _ in tokens:
    if tokval in keywords:
        print(f"Keyword: {tokval}")
    elif tokval in operators:
        print(f"Operator: {tokval}")
    elif tokval in delimiters:
        print(f"Delimiter: {tokval}")
    elif re.match("^[a-zA-Z_][a-zA-Z0-9_]*$", tokval):
        identifiers.add(tokval)
    elif re.match("^\\d+(\\.\\d+)?$", tokval):
        numbers.add(tokval)

for identifier in identifiers:
    print(f"Identifier: {identifier}")
for number in numbers:
    print(f"Number: {number}")
