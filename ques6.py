import itertools
import string
import time

def brute_force_attack(target_password):
    characters = string.ascii_lowercase
    password_length = 1

    while True:
        for guess in itertools.product(characters, repeat=password_length):
            guess = ''.join(guess)
            print(f"Trying: {guess}")

            if guess == target_password:
                return guess

        password_length += 1

target_password = "abc"

start_time = time.time()

found_password = brute_force_attack(target_password)

end_time = time.time()

print(f"Password '{found_password}' found in {end_time - start_time:.2f} seconds.")
