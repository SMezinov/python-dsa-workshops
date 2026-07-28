n = int(input())

stack = []
result = []

for _ in range(n):
    tag = input().strip()
    level = int(tag[1:])

    while len(stack) > 0 and stack[-1][1] >= level:
        closed_tag, _ = stack.pop()
        result.append(' ' * len(stack) + '</' + closed_tag + '>')

    result.append(' ' * len(stack) + '<' + tag + '>')
    stack.append([tag, level])

while len(stack) > 0:
    closed_tag, _ = stack.pop()
    result.append(' ' * len(stack) + '</' + closed_tag + '>')

print('\n'.join(result))
