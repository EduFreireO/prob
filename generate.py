import random
import faker


fake = faker.Faker()


names = set()

size = 1000

while len(names) < size:
    names.add(fake.name())

for name in names:
    print(name)
