import random
import string

def generate_random_emailid():
    username_length = random.randint(5, 10) 
    
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=username_length))

    domain=("@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com" )
    domain_random = random.choice(domain)

   
    email = f"{username}{domain_random}"

    return email


random_email = generate_random_emailid()
print(random_email)
