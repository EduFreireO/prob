from simples import sample
from read import read_estra


size_1 = 50
size_2 = 70
size_3 = 80

path = 'input/escola.in'
estratos = read_estra(size_1, size_2, size_3, path)

tamAmostra = 40
tamPop = 200
f = tamAmostra / tamPop

nES1 = int(size_1 * f)
nES2 = int(size_2 * f)
nES3 = int(size_3 * f)
 
est1 = sample(estratos[0], nES1)
est2 = sample(estratos[1], nES2)
est3 = sample(estratos[2], nES3)

file = open('output/estratificado.out', 'w')


file.write("\nPrimeiro Estrato\n")
for line in est1:
    file.write(line + '\n')


file.write("\nSegundo Estrato\n")
for line in est2:
    file.write(line + '\n')

file.write("\nTerceiro Estrato\n")
for line in est3:
    file.write(line + '\n')        



