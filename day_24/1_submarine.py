import re
import random
from collections import Counter


RE_NUM = re.compile("[-+]?\d+")
POP_SIZE = 1000
P_MUT = 0.17
LEN = 14
OFFSPRING_LEN = int(POP_SIZE * 0.8)
MAX_GENERATIONS = 2000
MAX = 1e15
SEED = 65537


def eval(code, input_, reg=None, start=0, end=None):
    input_ = list(input_)
    pc = start

    if end is None:
        end = len(code) - 1

    if reg is None:
        reg = {x: 0 for x in "wxyz"}

    cpu = {
        "inp": lambda *_: input_.pop(0),
        "add": lambda x, y: x + y,
        "mul": lambda x, y: x * y,
        "div": lambda x, y: x // y,
        "mod": lambda x, y: x % y,
        "eql": lambda x, y: int(x == y)
    }

    while pc <= end:
        inst, *args = code[pc]
        pc += 1
        r = args[0]
        l = None if len(args) < 2 else reg.get(args[1], args[1])

        reg[r] = cpu[inst](reg[r], l)

    return reg


def mate(a, b, p_mut=P_MUT, n=1):
    offspring = []

    for _ in range(n):
        i = random.randint(1, LEN - 1)
        offspring.extend([a[:i] + b[i:], b[:i] + a[i:]])

        if random.random() <= p_mut:
            offspring[-2:][random.randint(0, 1)][random.randint(0, LEN - 1)] = random.randint(1, 9)

    return offspring


TABLE = {}
def fitness(code, individual):
    ind = tuple(individual)
    if ind in TABLE:
        return TABLE[ind]

    result = eval(code, individual)['z']
    if not result:
        result -= int(as_str(individual))

    TABLE[ind] = result
    return result


def sort_population(code, population):
    population.sort(key=lambda x: fitness(code, x))
    return population


def as_str(ind):
    return "".join(str(x) for x in ind)


def new_gen(code, population, p_mut=P_MUT):
    offspring = []

    for i in range(OFFSPRING_LEN):
        a = population[random.randint(0, POP_SIZE - 1)]
        b = population[random.randint(0, POP_SIZE - 1)]
        offspring.extend(mate(a, b, p_mut))

    sort_population(code, population)
    population = population[:int(POP_SIZE * 0.20)] + offspring[:OFFSPRING_LEN]
    ind, c = Counter(tuple(x) for x in POPULATION).most_common()[0]
    if c > POP_SIZE * 0.1:
        population = [x for x in population if x != ind]
        while len(population) < POP_SIZE:
            a = population[random.randint(0, len(population) - 1)]
            b = population[random.randint(0, len(population) - 1)]
            population.extend(mate(a, b, p_mut=0.5, n=1))

    return population


random.seed(SEED)
data = open("input.txt").read()
POPULATION = [[random.randint(1, 9) for i in range(LEN)] for j in range(POP_SIZE)]
code = [tuple(int(x) if RE_NUM.match(x) else x for x in line.split()) for line in data.strip().split("\n")]
BEST = sort_population(code, population=POPULATION)[0]
MIN = fitness(code, BEST)

for i in range(MAX_GENERATIONS):
    POPULATION = new_gen(code, POPULATION, P_MUT)
    best = POPULATION[0]
    fit = fitness(code, best)
    if fit < MIN:
        MIN = fit
        BEST = best
        print(i, as_str(BEST), eval(code, best)['z'], MIN)
