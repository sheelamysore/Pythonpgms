import random
import string

def generate_random_email():
    username_length = random.randint(5, 10)  # Random length for username
    domain_length = random.randint(5, 10)  # Random length for domain

    # Generate random username
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=username_length))

    # Generate random domain
    domain = ''.join(random.choices(string.ascii_lowercase, k=domain_length))

    # Combine username and domain to form email
    email = f"{username}@{domain}.com"

    return email

# Example usage
random_email = generate_random_email()
print(random_email)
