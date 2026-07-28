students = list(map(int, input().split(' ')))
sandwiches = list(map(int, input().split(' ')))

counter = 0

while True:
    if len(students) == 0:
        print(0)
        break

    if counter == len(students):
        print(len(students))
        break

    if students[0] == sandwiches[0]:
        students.pop(0)
        sandwiches.pop(0)
        counter = 0
    else:
        temp = students.pop(0)
        students.append(temp)
        counter += 1
