import math
import random

# Hàm mã hóa dữ liệu từ file đầu vào và lưu vào file khác
def encrypt_file(input_file, output_file, public_key):
    with open(input_file, 'r') as file:
        message = file.read()
    
    message_ascii = [ord(c) for c in message]  # chuyển đổi các ký tự thành mã ASCII
    encrypted_message = [encrypt(m, *public_key) for m in message_ascii]  # mã hóa thông điệp

    with open(output_file, 'w') as file:
        file.write(' '.join(map(str, encrypted_message))) 

# Hàm giải mã dữ liệu từ file đầu vào và lưu vào file khác
def decrypt_file(input_file, output_file, private_key):
    with open(input_file, 'r') as file:
        encrypted_message = file.read().split()
        encrypted_message = [int(c) for c in encrypted_message]

    decrypted_message_ascii = [decrypt(c, private_key[0], private_key[1]) for c in encrypted_message] # giải mã thông điệp
    decrypted_message = ''.join([chr(c) for c in decrypted_message_ascii])  # chuyển đổi mã ASCII thành ký tự

    with open(output_file, 'w') as file:
        file.write(decrypted_message)

# Hàm tính ước chung lớn nhất
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Hàm kiểm tra số nguyên tố
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Hàm tìm số nguyên tố ngẫu nhiên trong khoảng [start, end]
def generate_prime(start, end):
    prime = random.randint(start, end)
    while not is_prime(prime):
        prime = random.randint(start, end)
    return prime

# Hàm tìm số e ngẫu nhiên và đảm bảo nó là số nguyên tố cùng nhau với phi_n, φ(n) = (p-1).(q-1) 
def generate_e(phi_n):
    while True:
        e = random.randint(2, phi_n)
        if gcd(e, phi_n) == 1:
            return e

# Hàm tìm số d sao cho (e * d) % phi_n = 1
def find_d(e, phi_n):
    d = pow(e, -1, phi_n)
    return d

# Hàm mã hóa thông điệp c = m^e mod n 

def encrypt(m, e, n):
    c = pow(m, e, n)
    return c

# Hàm giải mã thông điệp m = c^d mod n  

def decrypt(c, d, n):
    m = pow(c, d, n)
    return m

#1 Chọn hai số nguyên tố lớn----
p = generate_prime(100, 1000)
q = generate_prime(100, 1000)

#2 Tính n và phi(n)
n = p * q
phi_n = (p - 1) * (q - 1)

#3 Chọn số nguyên e
e = generate_e(phi_n)

#4 Tính số d
d = find_d(e, phi_n)

#5 Khóa công khai và khóa bí mật
public_key = (e, n)
private_key = (d, q, p)

# Mã hóa và giải mã thông điệp
print('Enter message:')
message = input()
message_ascii = [ord(c) for c in message] # chuyển đổi các ký tự thành mã 
encrypted_message = [encrypt(m, e, n) for m in message_ascii] # mã hóa thông điệp
decrypted_message_ascii = [decrypt(c, d, n) for c in encrypted_message] # giải mã thông điệp
decrypted_message = ''.join([chr(c) for c in decrypted_message_ascii]) # chuyển đổi mã  thành ký tự

print("public_key: ", public_key)
print("private_key: ", private_key)

input_file = 'input.doc'
output_file = 'output.doc'
decryptfile = 'decryptoutput.doc'
choice = 0
while True:
    print("1: Encrypt message")
    print("2: Decrypt message")
    print("3: Encrypt and save to file")
    print("4: Read decrypted file")
    print("5: Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Encrypted message:", encrypted_message)
        continue
    elif choice == 2:
        print("Decrypted message:", decrypted_message)
        continue
    elif choice == 3:
        # Gọi hàm mã hóa file
        encrypt_file(input_file, output_file, public_key)
        print("File encrypted and saved as", output_file)
        continue
    elif choice == 4:
        # Gọi hàm giải mã file
        decrypt_file(output_file, decryptfile, private_key)
        print("File decrypted and saved as", decryptfile)
        continue
    elif choice == 5:
        break
    else:
        print("Invalid choice. Please try again.")
