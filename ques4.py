import hashlib
import requests

def get_sha1_hash(password):
    return hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

def check_pwned_password(username, password):
    sha1_password = get_sha1_hash(password)
    prefix, suffix = sha1_password[:5], sha1_password[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise RuntimeError(f"Error fetching data: {response.status_code}")
    
    hashes = (line.split(':') for line in response.text.splitlines())
    
    for hash_suffix, count in hashes:
        if hash_suffix == suffix:
            return f"Password for '{username}' found {count} times in breaches!"
    
    return f"Password for '{username}' not found in any breaches."

def check_credentials_from_file(filename):
    try:
        with open(filename, 'r') as file:
            credentials = file.readlines()
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return

    for line in credentials:
        line = line.strip()
        if line:
            username, password = line.split(":")
            result = check_pwned_password(username, password)
            print(result)

filename = "credentials.txt"
check_credentials_from_file(filename)
