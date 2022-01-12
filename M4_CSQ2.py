n = int(input())
lst = input().split()

stack = []
for i in lst:
    if i == '+':
        stack[-2] = stack[-2] + stack[-1]
        stack.pop()
    elif i == '-':
        stack[-2] = stack[-2] - stack[-1]
        stack.pop()
    elif i == '*':
        stack[-2] = stack[-2] * stack[-1]
        stack.pop()
    elif i == '/':
        stack[-2] = stack[-2] / stack[-1]
        stack.pop()
    else:
        stack.append(int(i))

print(int(stack[0]))
