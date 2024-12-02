import numpy as np

def encryption(plain_text, depth):
    plain_text = plain_text.replace(" ", "")
    col = len(plain_text)
    arr = np.empty((depth, col), dtype='str')
    arr.fill("")  

    k = 0  
    j = 0  
    flag = 0  
    cipher = []

    for i in range(col):
        arr[j, i] = plain_text[k]  

        if j == depth - 1:
            flag = 1  
        elif j == 0:
            flag = 0  

        j += 1 if flag == 0 else -1
        k += 1  

    for i in range(depth):
        for j in range(col):
            if arr[i, j] != "":
                cipher.append(arr[i, j])

    return ''.join(cipher)

def decryption(cipher, depth):
    col = len(cipher)
    arr = np.empty((depth, col), dtype='str')
    arr.fill("*")  

    k = 0  
    j = 0  
    flag = 0  

    for i in range(col):
        if j < depth:
            arr[j, i] = '*'  

        if j == depth - 1:
            flag = 1  
        elif j == 0:
            flag = 0  

        j += 1 if flag == 0 else -1

    
    for i in range(depth):
        for j in range(col):
            if arr[i, j] == '*' and k < len(cipher):
                arr[i, j] = cipher[k]
                k += 1

    decrypted_text = []
    j = 0
    flag = 0
    
    for i in range(col):
        decrypted_text.append(arr[j, i])

        if j == depth - 1:
            flag = 1  
        elif j == 0:
            flag = 0  

        j += 1 if flag == 0 else -1

    return ''.join(decrypted_text)

def main():
    plain_text = "thank you very much"
    depth = 2  
    
    print("Encryption")
    cipher = encryption(plain_text, depth)
    print("Encrypted text:", cipher)
    
    print("Decryption")
    decrypted_text = decryption(cipher, depth)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":  
    main()
