
def first_task():
    n = int(input("Enter value to first task"))
    counter = 0
    i = 0
    while True:
        for j in range(i):
            print(i)
            counter = counter + 1
            if counter == n:
                break
        if counter == n:
            break
        i = i + 1


def second_task():
    inp = input("Enter the list of values to second task")
    x = int(input("Enter value to second task"))
    lst = map(int, inp.split())
    lst = list(lst)
    flag = False
    for i in range(len(lst)):
        if lst[i] == x:
            print(i)
            flag = True
    if not flag:
        print("Отсутствует")


def third_task():
    print("Enter values to third task")
    mx = []
    inp = 0
    while True:
        inp = input()
        if inp == "end":
            break
        lst = map(int, inp.split())
        mx.append(list(lst))
    print(mx)
    new_mx = []
    tmp_lst = []
    for i in range(len(mx)):
        tmp_lst.clear()
        for j in range(len(mx[i])):
            if i > 0:
                up = mx[i-1][j]
            else:
                up = mx[len(mx) - 1][j]

            if i < len(mx) - 1:
                down = mx[i+1][j]
            else:
                down = mx[0][j]

            if j > 0:
                left = mx[i][j-1]
            else:
                left = mx[i][len(mx[i]) - 1]

            if j < len(mx[i]) - 1:
                right = mx[i][j + 1]
            else:
                right = mx[i][0]
            tmp_lst.append(up + down + left + right)
        new_mx.append(tmp_lst.copy())
    print(new_mx)

def fourth_task():
    n = int(input("Enter value to fourth task"))
    if n < 0:
        print("Your number is negative, try again next time")
        return
    num = 0
    tmp = []
    res_mx = []
    for i in range(n):
        tmp.clear()
        for j in range(n):
            tmp.append(0)
        res_mx.append(tmp.copy())

    l = int(n/2)
    counter = 0
    for turns in range(l):
        for row in range(0 + turns, n - turns, 1):
            counter = counter + 1
            res_mx[turns][row] = counter
        for col in range(0 + turns + 1, n - turns, 1):
            counter = counter + 1
            res_mx[col][n - 1 - turns] = counter
        for row_l in range(n - 2 - turns, turns - 1, -1):
            counter = counter + 1
            res_mx[n - 1 - turns][row_l] = counter
        for col_l in range(n - 2 - turns, turns, -1):
            counter = counter + 1
            res_mx[col_l][turns] = counter
    if n % 2 == 1:
        res_mx[l][l] = n**2

    for i in range(len(res_mx)):
        print(res_mx[i], "\n")


def main():
    first_task()
    second_task()
    third_task()
    fourth_task()


if __name__ == "__main__":
    main()
