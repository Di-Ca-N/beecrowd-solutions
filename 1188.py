considerados = (
    (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6),
    (11, 7), (11, 8), (11, 9), (11, 10), (10, 2), (10, 3),
    (10, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9),
    (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8),
    (8, 4), (8, 5), (8, 6), (8, 7), (7, 5), (7, 6),
)

op = input()
total = 0
for i in range(12):
    for j in range(12):
        a = float(input())
        if (i, j) in considerados:
            total += a

if op == "S":
    print('{:.1f}'.format(total))

else:
    print('{:.1f}'.format(total / len(considerados)))
