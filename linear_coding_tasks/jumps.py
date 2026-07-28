n = int(input())
numbers = list(map(int, input().split()))

result = [0] * n

stack_nums = []
stack_results = []
max_result = 0

for i in range(n - 1, -1, -1):
    while len(stack_nums) > 0 and stack_nums[-1] <= numbers[i]:
        stack_nums.pop()
        stack_results.pop()

    if len(stack_nums) > 0:
        result[i] = stack_results[-1] + 1

    if result[i] > max_result:
        max_result = result[i]

    stack_nums.append(numbers[i])
    stack_results.append(result[i])

print(max_result)
print(' '.join(map(str, result)))