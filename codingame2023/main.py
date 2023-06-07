import sys
import math
from collections import defaultdict, deque

NUM_TARGET = 5

G = defaultdict(list)
eggs = defaultdict(int)
all_egg_cell = set()
crystals = defaultdict(int)
all_crystal_cell = set()

# amount of hexagonal cells in this map
number_of_cells = int(input())
for i in range(number_of_cells):
    # _type: 0 for empty, 1 for eggs, 2 for crystal
    # initial_resources: the initial amount of eggs/crystals on this cell
    # neigh_0: the index of the neighbouring cell for each direction
    _type, initial_resources, neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5 = map(int, input().split())
    print(_type, initial_resources, neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5, file=sys.stderr, flush=True)

    # set graph
    for neigh in (neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5):
        if neigh != -1:
            G[i].append(neigh)

    # set egg & crytal
    if _type == 1:
        eggs[i] = initial_resources
        all_egg_cell.add(i)
    elif _type == 2:
        crystals[i] = initial_resources
        all_crystal_cell.add(i)
print(G, file=sys.stderr, flush=True)
print("eggs:", eggs, file=sys.stderr, flush=True)
print("crystals:", crystals, file=sys.stderr, flush=True)

number_of_bases = int(input())
# my_base, opp_base
my_base_index_all = list(map(int, input().split()))
my_base_idx = my_base_index_all[0]
opp_base_index_all = list(map(int, input().split()))
opp_base_idx = opp_base_index_all[0]
print("base:", my_base_idx, opp_base_idx, file=sys.stderr, flush=True)

# ---------------------------------------------------
# output = [(14, 10), (6, 10)]
# -> print("BEACON", 14, 10, ";", "BEACON", 6, 10, ";")
def print_beacon(output):
    ans = []
    for (idx, ants) in output:
        ans.append("BEACON")
        ans.append(idx)
        ans.append(ants)
        ans.append(";")
    if ans:
        print(*ans)

def print_line(output):
    ans = []
    for (start, end, ants) in output:
        ans.append("LINE")
        ans.append(start)
        ans.append(end)
        ans.append(ants)
        ans.append(";")
    if ans:
        print(*ans)

# ---------------------------------------------------
def bfs(v):
    dist = [-1] * number_of_cells
    dist[v] = 1
    que = deque([])
    que.append(v)
    while que:
        v = que.popleft()
        for nv in G[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            que.append(nv)
    return dist

INF = float('inf')

# min dist from my base
min_dist_from_my_base = [INF] * number_of_cells
closest_base_idx = [None] * number_of_cells
for idx in my_base_index_all:
    each_dist = bfs(idx)
    # update min_dist_from_my_base & base_index
    for i in range(number_of_cells):
        if each_dist[i] < min_dist_from_my_base[i]:
            min_dist_from_my_base[i] = each_dist[i]
            closest_base_idx[i] = idx

# min dist from opp base
min_dist_from_opp_base = [INF] * number_of_cells
for idx in opp_base_index_all:
    each_dist = bfs(idx)
    # update min_dist_from_opp_base & base_index
    for i in range(number_of_cells):
        if each_dist[i] < min_dist_from_opp_base[i]:
            min_dist_from_opp_base[i] = each_dist[i]

# ---------------------------------------------------
# egg dist
eggs_dist_ordered = []
for cell, initial_resources in eggs.items():
    eggs_dist_ordered.append((min_dist_from_my_base[cell], min_dist_from_opp_base[cell], cell))
eggs_dist_ordered.sort(reverse=True)
print("eggs_dist_ordered:", eggs_dist_ordered, file=sys.stderr, flush=True)

# crystal dist
crystals_dist_ordered = []
for cell, initial_resources in crystals.items():
    crystals_dist_ordered.append((min_dist_from_my_base[cell], min_dist_from_opp_base[cell], cell))
crystals_dist_ordered.sort(reverse=True)
print("crystals_dist_ordered:", crystals_dist_ordered, file=sys.stderr, flush=True)

# egg & crystal dist : [far..<crystal>..near, far..<egg>..near]
# dist_ordered = []
# while crystals_dist_ordered:
#     dist_ordered.append(crystals_dist_ordered.pop())
# while eggs_dist_ordered:
#     dist_ordered.append(eggs_dist_ordered.pop())
# print("dist_ordered:", dist_ordered, file=sys.stderr, flush=True)

# calc eggs
total_amount_eggs = sum(v for v in eggs.values())
print("total amount of eggs:", total_amount_eggs, file=sys.stderr, flush=True)
get_amount_eggs = int(total_amount_eggs * 0.4)
print("get amount of eggs:", get_amount_eggs, file=sys.stderr, flush=True)

# ---------------------------------------------------
def is_egg_cell(cell):
    return cell in all_egg_cell

cand = []
is_egg_end = False

# game loop
while True:
    my_score, opp_score = map(int, input().split())
    print("my score:", my_score, " / opp score:", opp_score, file=sys.stderr, flush=True)

    egg_or_crystal_left = [0] * number_of_cells
    now_egg_total = 0
    now_my_ants_total = 0
    for i in range(number_of_cells):
        # resources: the current amount of eggs/crystals on this cell
        # my_ants: the amount of your ants on this cell
        # opp_ants: the amount of opponent ants on this cell
        resources, my_ants, opp_ants = map(int, input().split())
        print(i, ":", resources, my_ants, opp_ants, file=sys.stderr, flush=True)
        egg_or_crystal_left[i] = resources
        if i in all_egg_cell:
            now_egg_total += resources
        now_my_ants_total += my_ants

    # Write an action using print
    # WAIT | LINE <sourceIdx> <targetIdx> <strength> | BEACON <cellIdx> <strength> | MESSAGE <text>

    # erase 0 cell
    now_cand_len = len(cand)
    for _ in range(now_cand_len):
        if cand:
            target_cell = cand.pop()
            if is_egg_cell(target_cell) and is_egg_end:
                continue
            if egg_or_crystal_left[target_cell]:
                cand.insert(0, target_cell)
    print("cand (erase 0):", cand, file=sys.stderr, flush=True)

    # charge next cell
    if not is_egg_end:
        print("------------ egg -------------------", file=sys.stderr, flush=True)
        while eggs_dist_ordered:
            if len(cand) == 2:
                break
            dist_from_my_base, dist_from_opp_base, target_cell = eggs_dist_ordered.pop()
            # if get egg enough, not add cand
            if total_amount_eggs - now_egg_total >= get_amount_eggs:
                is_egg_end = True
                break
            # if less ants for reach, stop
            now_my_ants_total -= dist_from_my_base
            if (now_my_ants_total <= 0):
                eggs_dist_ordered.append((dist_from_my_base, dist_from_opp_base, target_cell))
                break
            # still left, append again
            if egg_or_crystal_left[target_cell]:
                cand.append(target_cell)
    else:
        print("------------ crystal -------------------", file=sys.stderr, flush=True)
        while crystals_dist_ordered:
            if len(cand) == 5:
                break
            dist_from_my_base, dist_from_opp_base, target_cell = crystals_dist_ordered.pop()
            # if less ants for reach, stop
            now_my_ants_total -= dist_from_my_base
            if (now_my_ants_total <= 0):
                crystals_dist_ordered.append((dist_from_my_base, dist_from_opp_base, target_cell))
                break
            # still left, append again
            if egg_or_crystal_left[target_cell]:
                cand.append(target_cell)
    print("cand:", cand, file=sys.stderr, flush=True)

    # output
    output = []
    for c in cand:
        output.append((closest_base_idx[c], c, 1))
    print_line(output)

    if not cand:
        print("WAIT")