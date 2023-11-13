import math
from read import read_name
from simples import sample
from scipy.stats import norm
from size_sample import calculate_sample_size



p = 0.5  
margin_of_error = 0.05  
confidence_level = 0.95 
population_size = 100  

sample_size = calculate_sample_size(p, margin_of_error, confidence_level, population_size)
print(sample_size)


male_list = read_name(100)
female_list = read_name(100)

male_list = sample(male_list, sample_size)
female_list = sample(female_list, sample_size)

for _ in male_list:
    print(_)


for _ in female_list:
     print(_)
    

