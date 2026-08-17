import random
import string

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits

all_chars = lowercase + uppercase + digits

p1 = random.choice(lowercase)
p2 = random.choice(uppercase)
p3 = random.choice(digits)

password_list = [p1, p2, p3]
for _ in range(9):
    password_list.append(random.choice(all_chars))

random.shuffle(password_list)

password = "".join(password_list)

print("Generated Password:", password)