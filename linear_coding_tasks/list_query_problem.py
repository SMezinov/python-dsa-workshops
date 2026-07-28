n = int(input().strip())

lists = []
for t in range(n):
    nums = list(map(int, input().strip().split()))
    _, *lst = nums
    lists.append(lst)

n2 = int(input().strip())

for t in range(n2):
    line, num = list(map(int, input().strip().split()))
    if line <= 0 or line > len(lists):
        print('ERROR!')
    elif num <= 0 or num > len(lists[line - 1]):
        print('ERROR!')
    else:
        print(lists[line - 1][num - 1])
