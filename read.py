def read_name(path):
    file = open(path, 'r')
    names = []
    for line in file:
        names.append(line)
    return names

def read_estra(size_1, size_2, size_3, path):
    file = open(path, 'r')
    estratos = [[], [], []]
    for _ in range(size_1):
        estratos[0].append(file.readline().split()[0])

    for _ in range(size_2):
        estratos[1].append(file.readline().split()[0])

    for _ in range(size_3):
        estratos[2].append(file.readline().split()[0])
    
    return estratos

