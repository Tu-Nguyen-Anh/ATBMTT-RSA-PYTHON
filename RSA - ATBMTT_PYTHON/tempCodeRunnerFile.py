m, e, n) for m in message_ascii] # mã hóa thông điệp
decrypted_message_ascii = [decrypt(c, d, n) for c in encrypted_message] # giải mã thông điệp
decrypted_message = ''.join([chr(c) for c in decrypted_message_ascii]) # chuyển đổi mã ASCII thành ký tự
