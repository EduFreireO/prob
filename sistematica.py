from random import randint
from read import read_name



input_size = 1000
names = read_name(input_size)

sample_size = 40


ratio = input_size // sample_size
first = randint(0, ratio - 1)

count = 1
for name in range(first, input_size - ratio, ratio):
    print(f'{names[name]} {count}')
    count += 1



