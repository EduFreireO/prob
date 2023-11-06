import math

def calculate_sample_size(population_size, confidence_level, margin_of_error):
    z_score = 0  # Valor Z para um determinado nível de confiança (95% por padrão)
    
    if confidence_level == 95:
        z_score = 1.96  # Valor Z para um nível de confiança de 95%
    elif confidence_level == 99:
        z_score = 2.58  # Valor Z para um nível de confiança de 99%
    
    sample_size = ((z_score**2) * (0.25) * (population_size)) / (margin_of_error**2)
    return math.ceil(sample_size)  # Arredonda para cima para garantir um número inteiro

# Exemplo de uso:
population_size = 1000
confidence_level = 95  # 95% de confiança
margin_of_error = 0.05  # 5% de margem de erro

sample_size = calculate_sample_size(population_size, confidence_level, margin_of_error)
print("Tamanho da amostra necessário:", sample_size)
