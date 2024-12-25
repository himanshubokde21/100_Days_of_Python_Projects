import re
from collections import deque

def Prefix(inEx):
    ex = '(' + inEx + ')'
    stack = []
    preEx = deque([])
    n = len(ex) - 1
    for p in range(n, -1, -1):
        if ex[p] == ')':
            stack.append(ex[p])
        elif ex[p] == '(':
            while stack and stack[-1] != ')':
                preEx.appendleft(stack.pop())
            stack.pop()
        elif re.match(r'[a-zA-Z0-9]', ex[p]):
            preEx.appendleft(ex[p])
        else:
            while (stack and stack[-1] != ')' and
                   priorities[ex[p]] < priorities[stack[-1]]):
                preEx.appendleft(stack.pop())
            stack.append(ex[p])
    return ''.join(preEx)

def Postfix(inEx):
    ex = '(' + inEx + ')'
    stack = []
    postEx = deque([])
    n = len(ex)
    for p in range(n):
        if ex[p] == '(':
            stack.append(ex[p])
        elif ex[p] == ')':
            while stack and stack[-1] != '(':
                postEx.append(stack.pop())
            stack.pop()
        elif re.match(r'[a-zA-Z0-9]', ex[p]):
            postEx.append(ex[p])
        else:
            while (stack and stack[-1] != '(' and
                   priorities[ex[p]] <= priorities[stack[-1]]):
                postEx.append(stack.pop())
            stack.append(ex[p])
    return ''.join(postEx)

validEx = r'^[A-Za-z0-9+\-*/()]+$'
priorities = {
    '^': 3,
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1
}

while True:
    inEx = input("Enter a 'Valid Infix Expression': ")
    inEx = inEx.replace(' ', '')
    if not re.match(validEx, inEx):
        print('Invalid Expression!\n')
    else:
        break

print('Prefix Expression: ', Prefix(inEx))
print('Postfix Expression: ', Postfix(inEx))
