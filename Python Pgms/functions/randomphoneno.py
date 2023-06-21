import random
import string

def generate_random_ph_num():
     
    first_part = str(random.randint(100, 999))

     
    second_part = str(random.randint(100, 999))

     
    third_part = str(random.randint(1000, 9999))

    phone_num = f"{first_part} {second_part} {third_part}"

    return phone_num


random_phone = generate_random_ph_num()
print(random_phone)
