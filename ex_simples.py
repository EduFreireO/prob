from simples import sample
from read import read_name
from size_sample import calculate_sample_size

input_size = 1000
names = read_name(input_size)


size = calculate_sample_size(1000, 95, 0.05)
set_of_names = sample(names, size)

for name in set_of_names:
    print(name)           


