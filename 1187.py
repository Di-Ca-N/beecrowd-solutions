considerados = (
    (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
    (0, 7), (0, 8), (0, 9), (0, 10), (1, 2), (1, 3),
    (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9),
    (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8),
    (3, 4), (3, 5), (3, 6), (3, 7), (4, 5), (4, 6),
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