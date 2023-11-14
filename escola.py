from read import read_name
from random import randint
names = read_name('input/nomes.txt')



q1 = 50
q2 = 70
q3 = 80



file = open("input/escola.in", 'w')
for _ in names:
    if q1:
        file.write(_[0 : len(_) - 1] + " " + str(randint(5, 9)))
        file.write('\n')
        q1-=1
    elif q2:
        file.write(_[0 : len(_) - 1] + " " + str(randint(10, 13)))
        file.write('\n')
        q2 -= 1
    else:
        
        file.write(_[0 : len(_) - 1] + " " + str(randint(14, 17)))
        file.write('\n')
        q3 -= 1
        
