from random import randint
from read import read_name


file = open('output/sistematica.out', 'w')


input_size = 1000
names = read_name('input/random.txt')  


sample_size = 40

K = input_size // sample_size
first = randint(0, K - 1)


for index in range(first, input_size, K):
    file.write(names[index])
    



