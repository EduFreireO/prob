import math
from scipy.stats import norm

def calculate_sample_size(p, margin_of_error, confidence_level, population_size):
    z_score = norm.ppf(1 - (1 - confidence_level) / 2)
    n0 = (z_score ** 2 * p * (1 - p)) / margin_of_error ** 2
    sample_size = (population_size * n0) / (population_size + n0 - 1)
    return math.ceil(sample_size)


