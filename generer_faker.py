from pprint import pprint
from faker import Faker

fake = Faker(locale="fr_FR")

pprint(dir(fake))
pprint(help(fake.file_path))

for _ in range(10):
    print(fake.unique.name())