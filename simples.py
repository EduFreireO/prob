from random import randint
def sample(names, sample_size):
    result = set()
    lastIndex = len(names) - 1
    while sample_size:
        index = randint(0, lastIndex)
        if names[index] not in result:
            result.add(names[index])
            sample_size -= 1
    return result




