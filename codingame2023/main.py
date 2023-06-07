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
    print(*ans)

def print_line(output):
    ans = []
    for (start, end, ants) in output:
        ans.append("LINE")
        ans.append(start)
        ans.append(end)
        ans.append(ants)
        ans.append(";")
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
dist = [INF] * number_of_cells
closest_base_idx = [None] * number_of_cells
for idx in my_base_index_all:
    each_dist = bfs(idx)
    # update min dist & closest base index
    for i in range(number_of_cells):
        if each_dist[i] < dist[i]:
            dist[i] = each_dist[i]
            closest_base_idx[i] = idx

# ---------------------------------------------------
# egg dist
eggs_dist_ordered = []
for cell, initial_resources in eggs.items():
    eggs_dist_ordered.append((dist[cell], cell))
eggs_dist_ordered.sort()
print("eggs_dist_ordered:", eggs_dist_ordered, file=sys.stderr, flush=True)

# crystal dist
crystals_dist_ordered = []
for cell, initial_resources in crystals.items():
    crystals_dist_ordered.append((dist[cell], cell))
crystals_dist_ordered.sort()
print("crystals_dist_ordered:", crystals_dist_ordered, file=sys.stderr, flush=True)

# egg & crystal dist : [far..<crystal>..near, far..<egg>..near]
dist_ordered = []
while crystals_dist_ordered:
    dist_ordered.append(crystals_dist_ordered.pop())
while eggs_dist_ordered:
    dist_ordered.append(eggs_dist_ordered.pop())

# calc eggs
total_amount_eggs = sum(v for v in eggs.values())
print("total amount of eggs:", total_amount_eggs, file=sys.stderr, flush=True)
get_amount_eggs = int(total_amount_eggs * 0.4)
print("get amount of eggs:", get_amount_eggs, file=sys.stderr, flush=True)

# ---------------------------------------------------
# create first candidate cell
cand = []
while dist_ordered:
    if len(cand) == NUM_TARGET:
        break
    _, target_cell = dist_ordered.pop()
    cand.append(target_cell)

# game loop
while True:
    egg_or_crystal_left = [0] * number_of_cells
    now_egg_total = 0
    for i in range(number_of_cells):
        # resources: the current amount of eggs/crystals on this cell
        # my_ants: the amount of your ants on this cell
        # opp_ants: the amount of opponent ants on this cell
        resources, my_ants, opp_ants = map(int, input().split())
        print(i, ":", resources, my_ants, opp_ants, file=sys.stderr, flush=True)
        egg_or_crystal_left[i] = resources
        if i in all_egg_cell:
            now_egg_total += resources

    # Write an action using print
    # WAIT | LINE <sourceIdx> <targetIdx> <strength> | BEACON <cellIdx> <strength> | MESSAGE <text>

    # erase 0 cell
    for _ in range(NUM_TARGET):
        if cand:
            target_cell = cand.pop()
            if egg_or_crystal_left[target_cell]:
                cand.insert(0, target_cell)

    # charge next cell
    while dist_ordered:
        if len(cand) == NUM_TARGET:
            break
        _, target_cell = dist_ordered.pop()
        # if get egg enough, not add cand
        if (target_cell in all_egg_cell) and (total_amount_eggs - now_egg_total >= get_amount_eggs):
            continue
        # still left, append again
        if egg_or_crystal_left[target_cell]:
            cand.append(target_cell)

    # output
    output = []
    for c in cand:
        output.append((closest_base_idx[c], c, 1))
    print_line(output)