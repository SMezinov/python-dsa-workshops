n = int(input())

lst = list(map(int, (input().strip().split(' '))))

q = int(input())

for t in range (q):
    cmd = input().strip().upper()
    if cmd == 'INSERT':
        pos, value = list(map(int, input().strip().split(' ')))
        if 0 <= pos <= len(lst):
            lst.insert(pos, value)

    if cmd == 'DELETE':
        pos = int(input())
        if 0 <= pos <= len(lst):
            lst.pop(pos)

print(*lst)