from simples import sample
from read import read_name



names = read_name('input/random.txt')


size_sample = 100
set_of_names = sample(names, size_sample)

file = open('output/eleicao.out', 'w')
for name in set_of_names:
    file.write(name)


