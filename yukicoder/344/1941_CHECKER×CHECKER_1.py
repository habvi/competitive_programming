T1 = [".#.", "#.#", ".#."]
T2 = ["#.#", ".#.", "#.#"]

S = [input() for _ in range(3)]
if S == T1 or S == T2:
    print('Yes')
else:
    print('No')