from random import randint
from read import read_name

def sample(names, sample_size):
    result = set()
    lastIndex = len(names) - 1
    while sample_size:
        index = randint(0, lastIndex)
        if names[index] not in result:
            result.add(names[index])
            sample_size -= 1
    return result

names = []
input_size = 1000


names = read_name(input_size)
set_of_names = sample(names, 10)

for name in set_of_names:
    print(name)           


