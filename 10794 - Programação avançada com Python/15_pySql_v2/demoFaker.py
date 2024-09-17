from faker import Faker

fake = Faker(locale='pt_PT')

print(fake.name())
print(type(fake.address()))

print(type(fake.phone_number()))