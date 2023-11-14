from random import randint

def sorteio(n, lower, upper):
    numbers = set()
    while len(numbers) < n:
        value = randint(lower, upper)
        if not value in numbers:
            numbers.add(value)
    return numbers

file = open("output/mega_sena.out", "w")
numbers = sorteio(6, 1, 60)

for number in numbers:
    line = str(number) + '\n'
    file.write(line)


        